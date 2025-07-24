import sqlite3
db = sqlite3.connect('hotel_management.db')
cursor = db.cursor()
results = cursor.execute('SELECT * FROM GUESTS').fetchall()

for i in results:
    print(i)

db.close()
