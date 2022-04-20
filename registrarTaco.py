
import os
from clasesTacos import *
from tacosCRUD import *

def registrarTaco():
  
  os.system("clear")
  print("---------------------")
  print("Registrar taco")
  print("---------------------")
  print("")
  
  tacoId = int(input("ID del taco: "));
  nombre = input("Nombre del taco: ");
  precio = float(input("Precio del taco: "));
  
  newTaco = Taco(tacoId, nombre, precio)
  createTaco(newTaco)
  
  print("")
  print("El taco se registró con exito")
  input("presiona una tecla para continuar...")
  
    