import sqlite3

import re #python -m flask run and ctrl c to quit

from flask import Flask, g, render_template

app = Flask(__name__)
DATABASE = "hotel_management.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g.database = sqlite3.connect(DATABASE)

    return db

def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():  
    return render_template("index.html")

@app.route("/Guests")
def guests(): 
    cursor = get_db.cursor()
    sql = "SELECT * FROM GUESTS;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("index.html", results=results)
