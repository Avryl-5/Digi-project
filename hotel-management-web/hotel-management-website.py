import sqlite3
db = sqlite3.connect('hotel_management.db')
cursor = db.cursor()
sql = "SELECT * FROM GUESTS;"
cursor.execute(sql)
results = cursor.fetchall()
for i in results:
    print(i)

db.close()
