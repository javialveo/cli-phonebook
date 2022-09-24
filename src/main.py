import ui as mui

APP_NAME = "cliPhoneBook"
APP_VERSION = "0.3.0"
APP_TITLE = f"{APP_NAME} v{APP_VERSION}"

def main():
  myUI = mui.UserInterface(APP_TITLE)
  
  userOption = 0
  endProgram = myUI.getExitOption()
  
  while userOption != endProgram:
    try:
      myUI.mainMenu()
      
      readOption = input(f"Opción [1:{endProgram}] ")
      userOption = int(readOption)
      
    except:
      print(f"\n\nPor favor ingresa un número entre 1 y {endProgram}")
      input("Pulsa ENTER para continuar")

main()
