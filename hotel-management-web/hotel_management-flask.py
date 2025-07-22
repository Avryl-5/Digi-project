import re #python -m flask run

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():  
    return render_template("index.html")

@app.route("/Guests")
def guests(): 
    import sqlite3
    db = sqlite3.connect('hotel_management.db')
    cursor = db.cursor()
    sql = "SELECT * FROM GUESTS;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        return(i)

    db.close()
