import sqlite3
db = sqlite3.connect('hotel_management.db')


#get everything about everyroom
Get_all_guests = db.cursor()
allguestsinfo = Get_all_guests.execute('SELECT * FROM GUESTS').fetchall()



#get everything about everyroom
get_all_rooms = db.cursor()
roomsinfo = get_all_rooms.execute('SELECT room_num, status_code FROM ROOMS').fetchall()
#for b in roomsinfo:
    #print(b)

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


#userinp2 = str(input("Name: "))

#Get_guest = db.cursor()
#guest_namel = guest_name.lower()
#guestinfo = Get_guest.execute("SELECT * FROM GUESTS WHERE ((LOWER(first_name ) LIKE '" + (str(guest_namel)) + "'|| '%') OR (LOWER(sur_name)  LIKE '" + (str(guest_namel)) + "'|| '%'));").fetchall()


#for h in guestinfo:
    #print(h)

#Get_room = db.cursor()
    
#foundmatches2 = Get_room.execute("SELECT room_num, status_code FROM ROOMS WHERE (room_num LIKE '" + (str(userinp2)) + "'|| '%');").fetchall()
#for i in foundmatches2:
    #print(i)


#get room acording to housekeeping status 
get_hkrooms = db.cursor()
hkroomsinfo = get_hkrooms.execute('SELECT room_num, housekeeping_code FROM ROOMS WHERE housekeeping_code = "HKP"').fetchall()
hkroomsinfo2 = get_hkrooms.execute('SELECT room_num, housekeeping_code FROM ROOMS WHERE housekeeping_code != "HKP"').fetchall()
hkcodes = get_hkrooms.execute('SELECT * FROM HOUSEKEEPINGS').fetchall()
#for j in hkroomsinfo:
 #   print(j)

#for k in hkcodes:
 #   print(k)

#for l in hkroomsinfo2:
 #   print(l)

get_reservation = db.cursor()
#resvtnids = get_reservation .execute('SELECT reservation_id FROM RESERVATIONS').fetchall()
#ridlist = []
guestidlist = []
#for m in resvtnids:
 #   ridlist.append(m[0])


#GRrelationship = get_reservation.execute("SELECT * FROM GUESTS_RESERVATIONS").fetchall()
rinfolist = []
#for c in GRrelationship:
 #   guestname = get_reservation.execute("SELECT first_name, sur_name FROM GUESTS WHERE guest_id = '" +(str(c[0]))+ "'").fetchall()
  #  dates = get_reservation.execute("SELECT * FROM RESERVATIONS WHERE reservation_id = '" +(str(c[1]))+ "'").fetchall()
   # for p in guestname:
    #    for r in dates:
     #       rinfolist.append((p[0], p[1], c[1], r[1], r[2]))

    
#for q in rinfolist:
    #print(q)
#print(rinfolist)




#RRrelationship = get_reservation.execute("SELECT * FROM ROOMS_RESERVATIONS").fetchall()
rinfolist = []
#for r in RRrelationship:
rrrealationship = get_reservation.execute("SELECT * FROM ROOMS_RESERVATIONS WHERE reservation_id ='" +(str(2))+ "'").fetchall()
for s in rrrealationship:
    roominfo = get_reservation.execute("SELECT * FROM ROOMS WHERE room_num = '" +(str(s[1]))+ "'").fetchall()


#for t in roominfo:
    #print(t)
#for q in rinfolist:
    #print(q)
#print(rinfolist)
gname = []
u=2
Rguests = get_reservation.execute("SELECT guest_id FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(u))+ "'").fetchall()
for v in Rguests:
    guestsinfo = get_reservation.execute("SELECT * FROM GUESTS WHERE guest_id = '" +(str(v[0]))+ "'").fetchall()
 #   print(guestsinfo[0])
    gname.append(guestsinfo[0])
#print(gname)
reservationsnums = get_reservation.execute("SELECT COUNT(reservation_id), * FROM RESERVATIONS ").fetchall()
#print(reservationsnums[0][0])
#for w in range(reservationsnums[0][0]):
  #  w +=1
    #GRrelationship = get_reservation.execute("SELECT COUNT(guest_id) FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(w))+ "'").fetchall()
   # res_info = get_reservation.execute("SELECT * FROM RESERVATIONS WHERE reservation_id = '" +(str(w))+ "'").fetchall()
    #print((res_info[0]) + (GRrelationship[0][0],))
   # print("next")
  #  print ((res_info[0][0]), (res_info[0][1]), (res_info[0][2]), (res_info[0][3]), (res_info[0][4]), (GRrelationship[0][0]))


#roomids = get_reservation.execute('SELECT room_num, status_code, room_type_id FROM ROOMS').fetchall()
#roominfo = []
#for ii in roomids:
#    rmtype = get_reservation.execute("SELECT * FROM ROOM_TYPES WHERE room_type_id = '" +(str(ii[2]))+ "'").fetchall()
#    print("here:", ii[0]) 
#    rmres = get_reservation.execute("SELECT reservation_id FROM ROOMS_RESERVATIONS WHERE room_num = ?", (ii[0],)).fetchall()
#    r_list = []
#    for r in rmres:
#        r_list.append(r[0])
#    print("---")
#    roominfo.append((ii[0],ii[1],rmtype[0][1],r_list))
#for iiii in roominfo:
#    print(iiii)

Get_all_guests = db.cursor()
gr_list = []
allguestsinfo = Get_all_guests.execute('SELECT * FROM GUESTS').fetchall()
for s in allguestsinfo:
    
   guest_res = Get_all_guests.execute("SELECT reservation_id FROM GUESTS_RESERVATIONS WHERE guest_id = '" +(str(s[0]))+ "'").fetchall()
   for t in guest_res:
       gr_list.append(tuple(s) + (t[0],))
    
#for i in gr_list:
 #   print(i)

get_reservation = db.cursor()
rinfolist = []
userinp3 = 2
GRrelationship = get_reservation.execute("SELECT COUNT(guest_id) FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(userinp3))+ "'").fetchall()
res_info = get_reservation.execute("SELECT * FROM RESERVATIONS WHERE reservation_id = '" +(str(userinp3))+ "'").fetchall()
#rinfolist.append(tuple(res_info[0]) + (GRrelationship[0][0],))



Due_arrivals = get_reservation.execute("SELECT * FROM RESERVATIONS WHERE (julianday(arrival_date) - julianday('2025-10-10'))>= 0 ORDER BY arrival_date").fetchall()
#for az in Due_arrivals:
    #print(az)

Due_departures = get_reservation.execute("SELECT * FROM RESERVATIONS WHERE (julianday(departure_date) - julianday('2025-10-10'))>= 0 ORDER BY departure_date").fetchall()
#for dz in Due_arrivals:
    #print(dz)
Guest_now = []
Get_now_res = get_reservation.execute("SELECT * FROM RESERVATIONS WHERE (julianday(arrival_date)<julianday('2025-10-10')) AND (julianday(departure_date)>julianday('2025-10-10'))").fetchall()
#for bz in Get_now_res:
 #   Get_now_gid = get_reservation.execute("SELECT guest_id FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(bz[0]))+ "'").fetchall()
    
  #  for cz in Get_now_gid:
       # Guest_now.append(cz)
#print(len(Guest_now))

available_rooms = get_reservation.execute("SELECT COUNT(room_num) FROM ROOMS WHERE status_code = 'VC'").fetchall()
#print(available_rooms)







get_roomtypes = db.cursor()
roomtypeinfo = get_roomtypes.execute('SELECT * FROM ROOM_TYPES').fetchall()
rtroom_list = []
for gz in roomtypeinfo:    
    how_many_room = get_reservation.execute("SELECT COUNT(room_num) FROM ROOMS WHERE room_type_id =  '" +(str(gz[0]))+ "'").fetchall()
    
    how_many_roomav = get_reservation.execute("SELECT COUNT(room_num) FROM ROOMS WHERE (room_type_id =  '" +(str(gz[0]))+ "') AND status_code = 'VC'").fetchall()
    rtroom_list.append((gz + (how_many_room[0][0],) + (how_many_roomav[0][0],)))


#print(rtroom_list)
userinp3 = 1

foundmatches3 = []
get_res = db.cursor()

res_info2 = get_res.execute("SELECT * FROM RESERVATIONS WHERE (reservation_id  LIKE '" + (str(userinp3)) + "'|| '%');").fetchall()
for kz in res_info2:
    
    GRrelationship2 = get_res.execute("SELECT COUNT(guest_id) FROM GUESTS_RESERVATIONS WHERE reservation_id  = '" + (str(kz[0])) + "'").fetchall()
    foundmatches3.append(tuple(kz) + (GRrelationship2[0][0],))

#for  i in foundmatches3:
  #  print(i)
print("----------------------")
order = 'arrival_date'
reservationsnums = get_reservation.execute("SELECT * FROM RESERVATIONS ORDER BY " +(str(order))+ "").fetchall()
for w in reservationsnums:
    GRrelationship = get_reservation.execute("SELECT COUNT(guest_id) FROM GUESTS_RESERVATIONS WHERE reservation_id = '" +(str(w[0]))+ "'").fetchall()
    
    rinfolist.append(tuple(w) + (GRrelationship[0][0],))

for  kz in rinfolist:
    print(kz)
db.close()
