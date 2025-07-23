import sqlite3

import re #python -m flask run and ctrl c to quit

from flask import Flask, g, render_template

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
    return render_template("index.html")

@app.route("/Guests")
def guests(): 
    db = get_db()
    all_guests = db.execute('SELECT * FROM GUESTS').fetchall()
    return all_guests
    