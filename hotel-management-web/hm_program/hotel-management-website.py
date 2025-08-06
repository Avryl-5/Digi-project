import sqlite3
db = sqlite3.connect('hotel_management.db')


#get everything about everyroom
Get_all_guests = db.cursor()
allguestsinfo = Get_all_guests.execute('SELECT * FROM GUESTS').fetchall()



#get everything about everyroom
get_all_rooms = db.cursor()
roomsinfo = get_all_rooms.execute('SELECT * FROM ROOMS').fetchall()
#for b in roomsinfo:
#    print(b)

#bridging ables
get_guestreservations = db.cursor()
GRrelationship = get_guestreservations.execute('SELECT * FROM GUESTS_RESERVATIONS').fetchall()
#for c in GRrelationship:
#    print(c)


get_roomreservations = db.cursor()
RRrelationship = get_roomreservations.execute('SELECT * FROM ROOMS_RESERVATIONS').fetchall()
#for d in RRrelationship:
#    print(d)

#statuses
get_statuses = db.cursor()
statuesinfo = get_statuses.execute('SELECT * FROM STATUS').fetchall()
#for e in statuesinfo:
#    print(e)


get_HKPingstatuses = db.cursor()
HKPingstatuesinfo = get_HKPingstatuses.execute('SELECT * FROM HOUSEKEEPINGS').fetchall()
#for f in HKPingstatuesinfo:
    #print(f)


#room types
get_roomtypes = db.cursor()
roomtypeinfo = get_roomtypes.execute('SELECT * FROM ROOM_TYPES').fetchall()
#for g in roomtypeinfo:
    #print(g)

#CUR_SOR = db.cursor()
#SQL_test = "SELECT id, test_name FROM TEST WHERE subject_id = '" + (str(w)) + "';"


guest_name = str(input("Name: "))

Get_guest = db.cursor()
guest_namel = guest_name.lower()
guestinfo = Get_guest.execute("SELECT * FROM GUESTS WHERE ((LOWER(first_name ) LIKE '" + (str(guest_namel)) + "'|| '%') OR (LOWER(sur_name)  LIKE '" + (str(guest_namel)) + "'|| '%'));").fetchall()


#for h in guestinfo:
    #print(h)


db.close()
