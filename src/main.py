import os

import database as mdb

APP_VERSION = "0.2.1"
APP_NAME = "cliPhoneBook"

TITLE_APP = f"{APP_NAME} v{APP_VERSION}"

MENU_LIST = [
  "1. Mostrar lista de contactos",
  "2. Registrar Contacto",
  "3. Salir"
]

COLUMN_LIST = {
  "id": "integer primary key autoincrement",
  "name": "string",
  "lastName": "string",
  "phoneNumber": "string",
  "email": "string"
}

def registerContact():
  print("\nRegistrar Contacto")
  
  name = input("Nombre: ")
  lastName = input("Apellido: ")
  telephone = input("Número de Teléfono: ")
  email = input("Correo Electrónico: ")
  
  contactInformation =[name, lastName, telephone, email]
  
  print(contactInformation)
  
  db = mdb.Database(APP_NAME, "database")
  db.insertValues(f"{APP_NAME.lower()}", contactInformation)
  
  input("\n\nPulsa ENTER para continuar")

def getExitMenu():
  exitOption = len(MENU_LIST)
  return exitOption

def setFirstConfiguration():
  databasePathExist = os.path.isdir("database")
  databaseExist = os.path.isfile(f"database/{APP_NAME}.db")
  
  if not(databaseExist):
    os.mkdir("database")

  if not(databaseExist):
    myDB = mdb.Database(APP_NAME, "database")
    myDB.createDataBase()
    myDB.createTable(f"{APP_NAME.lower()}", COLUMN_LIST)

def showContactList():
  db = mdb.Database(APP_NAME, "database")
  contactList = db.readValues(f"{APP_NAME.lower()}")

  if contactList == None:
    print("\n\nLa lista de contactos está vacía")
  else:
    arrayLength = len(contactList)

    print("\n\nID\tNombre\t\tApellido\tCelular  \tCorreo electrónico")
    for i in range(arrayLength):
      for information in contactList[i]:
        print(f"{information}   \t", end="")
      print("")
  
  input("\nPulsa ENTER para continuar")
  
def showMainMenu():
  print("\n"*20)
  print(f"\t\t{TITLE_APP}")

  print("Escoge una de las siguientes opciones disponibles")
  for menu in MENU_LIST:
    print(menu)

def main():
  setFirstConfiguration()
  userOption = 0
  while userOption != getExitMenu():
    try:
      showMainMenu()
      readOption = input(f"Opción [1-{getExitMenu()}]: ")
      userOption = int(readOption)
      
      if userOption == 1:
        showContactList()
      elif userOption == 2:
        registerContact()
    except ValueError:
      print(f"\n\nPor favor, ingresa un número entre 1 y {getExitMenu()}")
      input("Pulsa ENTER para continuar")


main()
