import sqlite3 as mdb

class Database:
  def __init__(self, namedb, databasePath):
    self.namedb = namedb
    self.databasePath = databasePath
  
  def __connectDatabase(self, sqlInstruction, getData=False, manyFields=False, valueList=""):
    data = []

    db = mdb.connect(f"{self.databasePath}/{self.namedb}.db")
    cur = db.cursor()

    if manyFields:
      cur.execute(sqlInstruction, valueList)
    else:
      cur.execute(sqlInstruction)

    if getData:
      data = cur.fetchall()
    
    db.commit()
    db.close

    if len(data) > 0:
      return data

  def createDataBase(self):
    db = mdb.connect(f"{self.databasePath}/{self.namedb}.db")
    db.commit()
    db.close()
    
  def createTable(self, nameTable, columnList):
    columns = ""
    
    for key, values in columnList.items():
      columns += f"{key} {values}, "
    
    sqlInstruction = f"create table {nameTable}({columns[:-2]})"
    
    self.__connectDatabase(sqlInstruction)

  def insertValues(self, nameTable, valuesList):
    sqlInstruction = f"insert into {nameTable} values(null, ?, ?, ?, ?)"

    self.__connectDatabase(sqlInstruction, False, True, valuesList)
  
  def readValues(self, nameTable, orderBy=None):
    sqlInstruction = ""
    dataFromDB = []

    if orderBy == None:
      sqlInstruction = f"select * from {nameTable}"
    else:
      sqlInstruction = f"select * from {nameTable} order by {orderBy}"
    
    dataFromDB = self.__connectDatabase(sqlInstruction, True)

    return dataFromDB
  
  def findValue(self, nameTable, columnName, value):
    sqlInstruction = f"select * from {nameTable} where {columnName} like '{value}%'"

    dataFromDB = self.__connectDatabase(sqlInstruction, True)

    return dataFromDB
  
  def updateValue(self, nameTable, columnName, newValue, referenceColumn, referenceValue):
    sqlInstruction = f"update {nameTable} set {columnName} = '{newValue}' where {referenceColumn} like '{referenceValue}'"
    
    self.__connectDatabase(sqlInstruction)
  
  def deleteValue(self, nameTable, columnName, value):
    sqlInstruction = f"delete from {nameTable} where {columnName} = {value}"

    self.__connectDatabase(sqlInstruction)
