import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')

def index():
    # open the connection to the database
    conn = sqlite3.connect('socio_economic_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Africa")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)
