class UserInterface:
  def __init__(self, titleApp):
    self.__menuList = (
      "1. Mostrar lista de contactos",
      "2. Salir"
    )
    
    self.__lineBreak = "\n" * 25
    self.__titleApp = titleApp
  
  def get_exit_option(self):
    exitOption = len(self.__menuList)
    return exitOption
  
  def main_menu(self):
    print(self.__lineBreak)
    print(f"\t\t{self.__titleApp}")
    print("\tAgenda de contactos en línea de comandos")
    
    print("\nEscoge una de las siguientes opciones disponibles")
    for menu in self.__menuList:
      print(menu)
  
  def view_contact(self, contactList=None):
    print(self.__lineBreak)
    print("Mostrando Lista de Contactos")
    
    if contactList != None:
      print("Nombre\t\tApellido\tCelular\t\t\tCorreo Electrónico")
      
      for myContacts in contactList:
        for contact in myContacts:
          print(f"{contact}", end="\t\t")
        print("")
    else:
      print("\n¡No hay contactos que mostrar!")
    input("\n\nPulsa ENTER para continuar")
