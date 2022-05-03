
from typing import List
from clasesTacos import *
from tacosCRUD import *

from rich.console import Console
from rich.table import Table

def verMenuTacos():
  tacosArr = getTacos()
  
  table = Table(title="Menu de Tacos", title_justify="left")
  table.add_column("ID", style="magenta", justify="center")
  table.add_column("Nombre", style="magenta", justify="center")
  table.add_column("Precio", style="magenta", justify="center")
  
  for taco in tacosArr:
    table.add_row(str(taco.tacoId), taco.nombre, str(taco.precio))
  console = Console()
  console.print(table)
  
  input("Presiona una tecla para continuar...")
