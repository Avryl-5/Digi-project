import re #python -m flask run and ctrl c to quit

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
    return render_template("index.html")

@app.route("/Guests")
def guests(): 
    db = get_db()
    Get_all_guests = db.cursor()
    allguestsinfo = Get_all_guests.execute('SELECT * FROM GUESTS').fetchall()
    
    return render_template("guestinfos.html", allguestsinfo=allguestsinfo)

@app.route("/foundguest", methods = ['POST'])
def foundguest():
    userinp = request.form["userinput"] 
    db = get_db()
    userinp = str(userinp.lower())
    Get_guest = db.cursor()
    
    foundmatches = Get_guest.execute("SELECT * FROM GUESTS WHERE ((LOWER(first_name ) LIKE '" + (str(userinp)) + "'|| '%') OR (LOWER(sur_name)  LIKE '" + (str(userinp)) + "'|| '%'));").fetchall()
    return render_template("guestsearch.html", foundmatches=foundmatches)
