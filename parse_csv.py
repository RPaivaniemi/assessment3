import csv
import sqlite3

conn = sqlite3.connect('socio_economic_data.db')
cur = conn.cursor()


conn.execute('DROP TABLE IF EXISTS Global')
print("table dropped successfully");

conn.execute('CREATE TABLE Global (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS Africa')
print("table dropped successfully");

conn.execute('CREATE TABLE Africa (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS Australasia')
print("table dropped successfully");

conn.execute('CREATE TABLE Australasia (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS Europe')
print("table dropped successfully");

conn.execute('CREATE TABLE Europe (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS LatinAmerica')
print("table dropped successfully");

conn.execute('CREATE TABLE LatinAmerica (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS MiddleEast')
print("table dropped successfully");

conn.execute('CREATE TABLE MiddleEast (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS NorthAmerica')
print("table dropped successfully");

conn.execute('CREATE TABLE NorthAmerica (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS SmallIslandStates')
print("table dropped successfully");

conn.execute('CREATE TABLE SmallIslandStates (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS TemperateAsia')
print("table dropped successfully");

conn.execute('CREATE TABLE TemperateAsia (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS TropicalAsia')
print("table dropped successfully");

conn.execute('CREATE TABLE TropicalAsia (Country TEXT, TotalPop TEXT, PopDens TEXT, GDP_Cap TEXT, GDP_Growth TEXT, LAND TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS individual')
print("table dropped successfully");
conn.execute('CREATE TABLE individual (Country TEXT, TotalPop TEXT, PopDens TEXT, ProjDens TEXT, UrbanPop TEXT, CoastalUrbanPop TEXT, GDP_Cap TEXT, GDP_Agric TEXT, GDP_Industry TEXT, GDP_Services TEXT, GDP_Growth TEXT, LAND TEXT, CropLAND TEXT, Pasture TEXT, ForestLAND TEXT, OtherLAND TEXT, WaterCAP TEXT, DomWithdraws TEXT, IndustryWithdraws TEXT, AgricWithdraws TEXT, IrrigatedLand TEXT, AgricLaborForce TEXT, CattleStock TEXT, SheepStock TEXT, GoatStock TEXT, PigStock TEXT, HorseStock TEXT, BuffaloStock TEXT, CamelStock TEXT, EnergyConsumption TEXT, FuelConsumption TEXT, HydroConsumption TEXT, KnownSpecies TEXT, EndemicSpecies TEXT, BirdSpecies TEXT, EndemicBirdSpecies TEXT, PlantSpecies TEXT, EndemicPlantSpecies TEXT)')
print("table created successfully");

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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        cur.execute('INSERT INTO Africa VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO Australasia VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO Europe VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        cur.execute('INSERT INTO LatinAmerica VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO MiddleEast VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO NorthAmerica VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO SmallIslandStates VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO TemperateAsia VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
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
        ProjDens = row[3]
        UrbanPop = row[4]
        CoastalUrbanPop = row[5]
        GDP_Cap = row[6]
        GDP_Agric = row[7]
        GDP_Industry = row[8]
        GDP_Services = row[9]
        GDP_Growth = row[10]
        LAND = row[11]
        CropLAND = row[12]
        Pasture = row[13]
        ForestLAND = row[14]
        OtherLAND = row[15]
        WaterCAP = row[16]
        DomWithdraws = row[17]
        IndustryWithdraws = row[18]
        AgricWithdraws = row[19]
        IrrigatedLand = row[20]
        AgricLaborForce = row[21]
        CattleStock = row[22]
        SheepStock = row[23]
        GoatStock = row[24]
        PigStock = row[25]
        HorseStock = row[26]
        BuffaloStock = row[27]
        CamelStock = row[28]
        EnergyConsumption = row[29]
        FuelConsumption = row[30]
        HydroConsumption = row[31]
        KnownSpecies = row[32]
        EndemicSpecies = row[33]
        BirdSpecies = row[34]
        EndemicBirdSpecies = row[35]
        PlantSpecies = row[36]
        EndemicPlantSpecies = row[37]

        cur.execute('INSERT INTO individual VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Country, TotalPop, PopDens, ProjDens, UrbanPop, CoastalUrbanPop, GDP_Cap, GDP_Agric, GDP_Industry, GDP_Services, GDP_Growth, LAND, CropLAND, Pasture, ForestLAND, OtherLAND, WaterCAP, DomWithdraws, IndustryWithdraws, AgricWithdraws, IrrigatedLand, AgricLaborForce, CattleStock, SheepStock, GoatStock, PigStock, HorseStock, BuffaloStock, CamelStock, EnergyConsumption, FuelConsumption, HydroConsumption, KnownSpecies, EndemicSpecies, BirdSpecies, EndemicBirdSpecies, PlantSpecies, EndemicPlantSpecies))
        cur.execute('INSERT INTO TropicalAsia VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        cur.execute('INSERT INTO Global VALUES (?,?,?,?,?,?)', (Country, TotalPop, PopDens, GDP_Cap, GDP_Growth, LAND))
        conn.commit()
      except Exception:
        pass
    else:
      break

print("Data parsed successfully");
conn.close()