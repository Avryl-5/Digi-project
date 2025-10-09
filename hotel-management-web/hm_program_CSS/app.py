import re #python -m flask run and ctrl c to quit work

from flask import Flask, g, render_template, request

import sqlite3

app = Flask(__name__)
DATABASE = "hotel_management.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route("/")
def home():  
    db = get_db()
    get_all_hm = db.cursor()
    
    Due_arrivals = get_all_hm.execute("SELECT * FROM RESERVATIONS WHERE (julianday(arrival_date) - julianday('2025-10-10'))>= 0 ORDER BY arrival_date LIMIT 5 ").fetchall()

    Due_departures = get_all_hm.execute("SELECT * FROM RESERVATIONS WHERE (julianday(departure_date) - julianday('2025-10-10'))>= 0 ORDER BY departure_date LIMIT 5 ").fetchall()
    
        
    Guest_now = []
    Get_now_res = get_all_hm.execute("SELECT * FROM RESERVATIONS WHERE (julianday(arrival_date)<julianday('2025-10-10')) AND (julianday(departure_date)>julianday('2025-10-10'))").fetchall()
    for bz in Get_now_res:
        Get_now_gid = get_all_hm.execute("SELECT guest_id FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(bz[0]))+ "'").fetchall()
    
        for cz in Get_now_gid:
            Guest_now.append(cz)
    Guest_now = len(Guest_now)

    available_rooms = get_all_hm.execute("SELECT COUNT(room_num) FROM ROOMS WHERE status_code = 'VC'").fetchall()
    

    return render_template("index.html",Due_arrivals=Due_arrivals, Due_departures=Due_departures, available_rooms=available_rooms, Guest_now=Guest_now)

@app.route("/Guests")
def guests(): 
    db = get_db()
    Get_all_guests = db.cursor()
    gr_list = []
    allguestsinfo = Get_all_guests.execute('SELECT * FROM GUESTS').fetchall()
    for s in allguestsinfo:
    
       guest_res = Get_all_guests.execute("SELECT reservation_id FROM GUESTS_RESERVATIONS WHERE guest_id = '" +(str(s[0]))+ "'").fetchall()
       for t in guest_res:
           gr_list.append(tuple(s) + (t[0],))
    
    return render_template("guestinfos.html", gr_list=gr_list)

@app.route("/foundguest", methods = ['POST'])
def foundguest():
    userinp = request.form["userinput"] 
    db = get_db()
    userinp = str(userinp.lower())
    Get_guest = db.cursor()
    
    foundmatches = Get_guest.execute("SELECT * FROM GUESTS WHERE ((LOWER(first_name ) LIKE '" + (str(userinp)) + "'|| '%') OR (LOWER(sur_name)  LIKE '" + (str(userinp)) + "'|| '%') OR (guest_id  LIKE '" + (str(userinp)) + "'|| '%'));").fetchall()
    return render_template("guestinfos.html", foundmatches=foundmatches)

@app.route("/Roomtypes")
def room_types():
    db = get_db()
    get_roomtypes = db.cursor()
    roomtypeinfo = get_roomtypes.execute('SELECT * FROM ROOM_TYPES').fetchall()
    rtroom_list = []
    for gz in roomtypeinfo:    
        how_many_room = get_roomtypes.execute("SELECT COUNT(room_num) FROM ROOMS WHERE room_type_id =  '" +(str(gz[0]))+ "'").fetchall()
    
        how_many_roomav = get_roomtypes.execute("SELECT COUNT(room_num) FROM ROOMS WHERE (room_type_id =  '" +(str(gz[0]))+ "') AND status_code = 'VC'").fetchall()
        rtroom_list.append((tuple(gz) + (how_many_room[0][0],) + (how_many_roomav[0][0],)))
        
    return render_template("roomtypes.html", rtroom_list=rtroom_list)

@app.route("/Rooms")
def rooms():
    db = get_db()
    get_room = db.cursor()
    
    statuses = get_room.execute("SELECT * FROM STATUS").fetchall()

    VC_rooms = get_room.execute("SELECT COUNT(room_num) FROM ROOMS WHERE status_code = 'VC'").fetchall()

    VD_rooms = get_room.execute("SELECT COUNT(room_num) FROM ROOMS WHERE status_code = 'VD'").fetchall()

    OC_rooms = get_room.execute("SELECT COUNT(room_num) FROM ROOMS WHERE status_code = 'OC'").fetchall()

    NS_rooms = get_room.execute("SELECT COUNT(room_num) FROM ROOMS WHERE status_code = 'NS'").fetchall()

    OOO_rooms = get_room.execute("SELECT COUNT(room_num) FROM ROOMS WHERE status_code = 'OOO'").fetchall()

    roominfo = []
    rooms = get_room.execute('SELECT room_num, status_code, room_type_id FROM ROOMS').fetchall()
    for ii in rooms:
        rmtype = get_room.execute("SELECT * FROM ROOM_TYPES WHERE room_type_id = '" +(str(ii[2]))+ "'").fetchall()

        rmres = get_room.execute("SELECT reservation_id FROM ROOMS_RESERVATIONS WHERE room_num = '" +(str(ii[0]))+ "'").fetchall()
        r_list = []
        for r in rmres:
            r_list.append(r[0])
        roominfo.append((ii[0],ii[1],rmtype[0][1],r_list))
    return render_template("rooms.html", statuses=statuses, roominfo=roominfo, VC_rooms=VC_rooms[0][0], VD_rooms=VD_rooms[0][0], OC_rooms=OC_rooms[0][0], NS_rooms=NS_rooms[0][0], OOO_rooms=OOO_rooms[0][0])

@app.route("/foundrooms", methods = ['POST'])
def foundrooms():
    userinp2 = request.form["userinput2"] 
    db = get_db()
    Get_room = db.cursor()
    
    foundmatches2 = Get_room.execute("SELECT room_num, status_code FROM ROOMS WHERE (room_num LIKE '" + (str(userinp2)) + "'|| '%');").fetchall()
    return render_template("rooms.html", foundmatches2=foundmatches2)

@app.route("/Housekeeping")
def housekeeping():
    db = get_db()
    get_housekeepingcodes = db.cursor()
    hkcodes = get_housekeepingcodes.execute('SELECT * FROM HOUSEKEEPINGS').fetchall()
    hkproomsinfo = get_housekeepingcodes.execute('SELECT room_num, housekeeping_code FROM ROOMS WHERE housekeeping_code = "HKP"').fetchall()
    otherhkrooms = get_housekeepingcodes.execute('SELECT room_num, housekeeping_code FROM ROOMS WHERE housekeeping_code != "HKP"').fetchall()
    return render_template("housekeeping.html", hkcodes=hkcodes , hkproomsinfo=hkproomsinfo, otherhkrooms=otherhkrooms)


@app.route("/Reservations")
def Reservation():
    order = request.args.get('order', 'reservation_id')
    db = get_db()
    get_reservation = db.cursor()
    rinfolist = []
    
    reservationsnums = get_reservation.execute("SELECT * FROM RESERVATIONS ORDER BY " +(str(order))+ "").fetchall()
    for w in reservationsnums:
        GRrelationship = get_reservation.execute("SELECT COUNT(guest_id) FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(w[0]))+ "'").fetchall()
    
        rinfolist.append(tuple(w) + (GRrelationship[0][0],))
            

    return render_template("reservations.html", rinfolist=rinfolist)


@app.route("/foundres", methods = ['GET','POST'])
def foundres():
    if request.method == "POST":
        userinp3 = request.form["userinput3"] 
    else:
        userinp3 = request.args.get('res_id')
    foundmatches3 = []
    db = get_db()
    get_res = db.cursor()
    res_info2 = get_res.execute("SELECT * FROM RESERVATIONS WHERE (reservation_id  LIKE '" + (str(userinp3)) + "'|| '%');").fetchall()
    for kz in res_info2:
        GRrelationship2 = get_res.execute("SELECT COUNT(guest_id) FROM GUESTS_RESERVATIONS WHERE reservation_id  = '" + (str(kz[0])) + "'").fetchall()
        foundmatches3.append(tuple(kz) + (GRrelationship2[0][0],))

    return render_template("reservations.html", foundmatches3=foundmatches3)


@app.route("/Reservations_details/<res_id>, methods = ['GET', 'POST'])")
def Reservation_detail(res_id):
    Arivald = request.args.get('Arivald')
    Departd = request.args.get('Departd')
    kid_num = request.args.get('kid_num')
    adult_num = request.args.get('adult_num')
    totalg = request.args.get('totalg')
    db = get_db()
    get_reservation = db.cursor()
    roominfo =[]
    rrrealationship = get_reservation.execute("SELECT * FROM ROOMS_RESERVATIONS WHERE reservation_id ='" +(str(res_id))+ "'").fetchall()
    for s in rrrealationship:
        roominfos = get_reservation.execute("SELECT * FROM ROOMS WHERE room_num = '" +(str(s[1]))+ "'").fetchall()
        roominfo.extend(roominfos)
    

    gname = []

    Rguests = get_reservation.execute("SELECT guest_id FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(res_id))+ "'").fetchall()
    for v in Rguests:
        guestsinfo = get_reservation.execute("SELECT * FROM GUESTS WHERE guest_id = '" +(str(v[0]))+ "'").fetchall()
        gname.append(guestsinfo[0])
    


    return render_template("resvtndetails.html", roominfo=roominfo, gname=gname,
    res_id=res_id, Arivald=Arivald, Departd=Departd, kid_num=kid_num, adult_num=adult_num, totalg=totalg)

