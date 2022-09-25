class UserInterface:
  def __init__(self, titleApp):
    self.__menuList = (
      "1. Mostrar lista de contactos",
      "2. Salir"
    )
    
    self.__lineBreak = "\n" * 20
    self.__titleApp = titleApp
  
  def getExitOption(self):
    exitOption = len(self.__menuList)
    return exitOption
  
  def mainMenu(self):
    print(self.__lineBreak)
    print(f"\t\t{self.__titleApp}")
    print("\tAgenda de contactos en línea de comandos")
    
    print("\nEscoge una de las siguientes opciones disponibles")
    for menu in self.__menuList:
      print(menu)
