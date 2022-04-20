
import json
from clasesTacos import *
from typing import List, Dict

def getTacos() -> List[Taco]:
  listaTacos: List[Taco] = []
  
  with open("tacos-data.json") as json_file:
    tacosArr  = json.load(json_file)
    
    for taco in tacosArr:
      tacoId = taco["tacoId"]
      nombre = taco["nombre"]
      precio = taco["precio"]
      
      listaTacos.append(Taco(tacoId, nombre, precio))
  return listaTacos

def createTaco(tacoData: Taco):
  tacosArr: List[Dict] = []
  
  with open("tacos-data.json") as json_file:
    tacosArr  = json.load(json_file)
    
  tacosArr.append(tacoData.__dict__)
  
  with open("tacos-data.json", "w") as json_file:
    json.dump(tacosArr, json_file, indent=2, separators=(',', ': '))