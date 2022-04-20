
import os
from venderTacos import *
from registrarTaco import *
from verMenuTacos import *

def main():
  salirTrue = False
  opcionSalir = 4
  
  while(not salirTrue):
    
    os.system("clear")
    
    print("")
    print("---------------------")
    print("Bienvenido a taqueria")
    print("---------------------")
    print("")
    print("1. Vender tacos")
    print("2. Registrar taco")
    print("3. Ver menu de tacos")
    print(f"{opcionSalir}. Salir")
    print("")
    respuesta = int(input("Digite la opción: "))
    
    os.system("clear")
    
    if(respuesta == 1):
      venderTacos()
      
    elif(respuesta == 2):
      registrarTaco()
      
    elif(respuesta == 3):
      verMenuTacos()
    
    elif(respuesta == opcionSalir):
      salirTrue = True
      
    else:
      print("Opción incorrecta")
      input("Pulse una tecla para continuar...")
      
main()