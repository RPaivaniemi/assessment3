import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')

def index():
    # open the connection to the database
    conn = sqlite3.connect('socio_economic_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from Global")
    #rows = cur.fetchall()
    #cur.execute("select * from Australasia")
    #rows = cur.fetchall()
    #cur.execute("select * from Europe")
    #rows = cur.fetchall()
    #cur.execute("select * from LatinAmerica")
    #rows = cur.fetchall()
    #cur.execute("select * from MiddleEast")
    #rows = cur.fetchall()
    #cur.execute("select * from NorthAmerica")
    #rows = cur.fetchall()
    #cur.execute("select * from SmallIslandStates")
    #rows = cur.fetchall()
    #cur.execute("select * from TemperateAsia")
    #rows = cur.fetchall()
    #cur.execute("select * from TropicalAsia")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/Africa')
def africa():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from Africa")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/Australasia')
def australasia():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from Australasia")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/Europe')
def europe():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from Europe")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/LatinAmerica')
def latinamerica():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from LatinAmerica")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/MiddleEast')
def middleeast():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from MiddleEast")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/NorthAmerica')
def northamerica():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from NorthAmerica")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/SmallIslandStates')
def smallislandstates():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from SmallIslandStates")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/TemperateAsia')
def temperateasia():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from TemperateAsia")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/TropicalAsia')
def tropicalasia():
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from TropicalAsia")
  rows = cur.fetchall()
  conn.close()
  return render_template('index.html', rows=rows)

@app.route('/show/<Country>')
def show(Country):
  conn = sqlite3.connect('socio_economic_data.db')
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  cur.execute("select * from individual WHERE Country =?", (Country,),)
  rows = cur.fetchall()
  conn.close()
  return render_template('show.html', rows=rows, Country=Country)
