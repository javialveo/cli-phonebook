import os as mos
import sqlite3 as mdb

class Database:
  def __init__(self, namedb, databasePath):
    self.__namedb = namedb
    self.__databasePath = databasePath
    self.__tableName = "contactos"
    self.__columnList = { 
      "id": "integer primary key",
      "name": "string",
      "lastName": "string",
      "phoneNumber": "string",
      "email": "string"
    }
  
  def checkDatabaseExists(self):
    databasePathExists = mos.path.isdir(self.__databasePath)
    databaseExists = mos.path.isfile(f"{self.__databasePath}/{self.__namedb}.db")

    if not(databasePathExists):
      mos.mkdir(self.__databasePath)
    
    if not(databaseExists):
      self.createDatabase()
      self.createTable()
    
  def createDatabase(self):
    db = mdb.connect(f"{self.__databasePath}/{self.__namedb}.db")
    db.commit
    db.close()
  
  def createTable(self):
    columns = ""

    for key, values in self.__columnList.items():
      columns += f"{key} {values}, "
    
    sqlStatement = f"create table {self.__tableName} ({columns[:-2]})"

    db = mdb.connect(f"{self.__databasePath}/{self.__namedb}.db")
    cur = db.cursor()
    cur.execute(sqlStatement)
    db.commit()
    db.close()

