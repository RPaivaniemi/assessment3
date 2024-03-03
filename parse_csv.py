import csv
import sqlite3

conn = sqlite3.connect('socio_economic_data.db')
cur = conn.cursor()


conn.execute('DROP TABLE IF EXISTS Global')
print("table dropped successfully");

conn.execute('CREATE TABLE Global (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS Australasia')
#print("table dropped successfully");

#conn.execute('CREATE TABLE Australasia (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS Europe')
#print("table dropped successfully");

#conn.execute('CREATE TABLE Europe (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS LatinAmerica')
#print("table dropped successfully");

#conn.execute('CREATE TABLE LatinAmerica (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS MiddleEast')
#print("table dropped successfully");

#conn.execute('CREATE TABLE MiddleEast (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS NorthAmerica')
#print("table dropped successfully");

#conn.execute('CREATE TABLE NorthAmerica (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS SmallIslandStates')
#print("table dropped successfully");

#conn.execute('CREATE TABLE SmallIslandStates (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS TemperateAsia')
#print("table dropped successfully");

#conn.execute('CREATE TABLE TemperateAsia (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

#conn.execute('DROP TABLE IF EXISTS TropicalAsia')
#print("table dropped successfully");

#conn.execute('CREATE TABLE TropicalAsia (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
#print("table created successfully");

with open('Database/Socio-Economic_Baseline_Data_Africa.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

with open('Database/Socio-Economic_Baseline_Data_Australasia.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

    cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
    conn.commit()

with open('Database/Socio-Economic_Baseline_Data_Europe.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

with open('Database/Socio-Economic_Baseline_Data_LatinAmerica.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

with open('Database/Socio-Economic_Baseline_Data_MiddleEast.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break
  
with open('Database/Socio-Economic_Baseline_Data_NorthAmerica.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

with open('Database/Socio-Economic_Baseline_Data_SmallIslandStates.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

with open('Database/Socio-Economic_Baseline_Data_TemperateAsia.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

with open('Database/Socio-Economic_Baseline_Data_TropicalAsia.csv', newline='') as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)
    if row[0]:
      try:
        Country = row[0]
        TotalPop = row[1]
        PopDens = row[2]
        GDP_Cap = row[6]
        GDP_Growth = row[10]
        LAND = row[11]

        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

print("Data parsed successfully");
conn.close()