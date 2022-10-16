import database as mdb
import ui as mui

APP_NAME = "cliPhoneBook"
APP_VERSION = "0.3.1"
APP_TITLE = f"{APP_NAME} v{APP_VERSION}"

def set_first_configuration():
  db = mdb.Database("cliphonebook", "database")
  db.check_database_exists()

def show_contacts():
  myUI = mui.UserInterface(APP_TITLE)
  db = mdb.Database("cliphonebook", "database")
  
  datos = db.get_all_data()
  
  myUI.view_contact(datos)

def main():
  set_first_configuration()
  
  myUI = mui.UserInterface(APP_TITLE)
  
  userOption = 0
  endProgram = myUI.get_exit_option()
  
  while userOption != endProgram:
    try:
      myUI.main_menu()
      
      readOption = input(f"Opción [1:{endProgram}] ")
      userOption = int(readOption)
      
      if userOption == 1:
        show_contacts()
    except ValueError:
      print(f"\n\nPor favor ingresa un número entre 1 y {endProgram}")
      input("Pulsa ENTER para continuar")

main()
