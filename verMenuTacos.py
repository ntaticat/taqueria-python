
from typing import List
from clasesTacos import *
from tacosCRUD import *

def verMenuTacos():
  tacosArr = getTacos()
  print("---------------------")
  print("Menu de Tacos")
  print("---------------------")
  print("")
  for taco in tacosArr:
    print(f"--> id: {taco.tacoId} - tipo: {taco.nombre} - precio: ${taco.precio}")
  print("")
  input("Presiona una tecla para continuar...")
      
      