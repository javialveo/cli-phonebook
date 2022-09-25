import os as mos
import sqlite3 as mdb

class Database:
  def __init__(self, namedb, databasePath):
    self.__namedb = namedb
    self.__databasePath = databasePath
    self.__tableName = "contactos"
  
  def checkDatabaseExists(self):
    databasePathExists = mos.path.isdir(self.__databasePath)
    databaseExists = mos.path.isfile(f"{self.__databasePath}/{self.__namedb}.db")

    if not(databasePathExists):
      mos.mkdir(self.__databasePath)
    
    if not(databaseExists):
      self.__createDatabase()
      self.__createTable()
    
  def __createDatabase(self):
    db = mdb.connect(f"{self.__databasePath}/{self.__namedb}.db")
    db.commit
    db.close()
  
  def __createTable(self):
    columns = ""
    fieldList = (
      "id integer not null primary key", 
      "name string", 
      "lastName string", 
      "phoneNumber string", 
      "email string"
    )
    
    listLength = len(fieldList)

    for i in range(listLength):
      columns += fieldList[i]

      if i < listLength-1:
        columns += ", "
    
    sqlStatement = f"create table {self.__tableName} ({columns})"
    
    db = mdb.connect(f"{self.__databasePath}/{self.__namedb}.db")
    cur = db.cursor()
    cur.execute(sqlStatement)
    db.commit()
    db.close()
  
  def getAllData(self, orderBy=None):
    db = mdb.connect(f"{self.__databasePath}/{self.__namedb}.db")
    cur = db.cursor()
    
    if orderBy != None:
      cur.execute(f"select name, lastName, phoneNumber, email from {self.__tableName} order by {orderBy}")
    else:
      cur.execute(f"select name, lastName, phoneNumber, email from {self.__tableName}")
    
    data = cur.fetchall()
    
    db.commit()
    db.close()
    
    if len(data) > 0:
      return data
    else:
      return None

