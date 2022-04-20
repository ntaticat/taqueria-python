
import os
from clasesTacos import *
from tacosCRUD import *
from typing import List
  

def venderTacos():
  
  tacos: List[Taco] = getTacos()
  
  terminarCompra = False
  
  pedidoObj = Pedido(1, 0, [])
  
  while(not terminarCompra):
    
    os.system("clear")
    
    print("---------------------")
    print("Venta de tacos")
    print("---------------------")
    print("")
    print("Tacos registrados en el pedido: ")
    print("")
    
    if(len(pedidoObj.pedidosTacos) > 0):
      for tacoPedido in pedidoObj.pedidosTacos:
        totalTacoIndividual = tacoPedido.cantidad * tacoPedido.taco.precio
        print(f"--> {tacoPedido.taco.nombre} - {tacoPedido.cantidad} x ${tacoPedido.taco.precio} = ${ totalTacoIndividual }")  
    else:
      print("--> No hay tacos registrados")
    
    print("")
    if(len(pedidoObj.pedidosTacos) > 0):
      print(f"Total del pedido: ${pedidoObj.total}")
      print("")
      
    print("---------------------")
    print("")
    print("Opciones a seleccionar: ")
    print("")
    print("1. Registrar cantidad de un tipo de taco")
    print("2. Registrar venta")
    print("3. Salir sin registrar venta")
    print("")
    print("---------------------")
    print("")
    
    opcionCompra = int(input("Digite la opción deseada: "))
    
    if(opcionCompra == 3):
      terminarCompra = True
      
    elif(opcionCompra == 2):
      os.system("clear")
      
      print("---------------------")
      print("Registro de Pedido")
      print("---------------------")
      
      print("")
      print("Pedido realizado")
      print("")
      
      print("Gracias por su compra")
      input("Presione una tecla para continuar...")
      terminarCompra = True
      
    else:
      os.system("clear")
      
      print("---------------------")
      print("Menu de Tacos")
      print("---------------------")
      print("")
      for taco in tacos:
        print(f"--> id: {taco.tacoId} - tipo: {taco.nombre} - precio: ${taco.precio}")
        
      print("")
      idTaco = int(input("Digite el ID del taco: "))
      
      tacoYaRegistrado = False
      tacoPedidoRegistrado = None
      
      # Existe el taco en el pedido
      for pedidoTaco in pedidoObj.pedidosTacos:
        if(pedidoTaco.taco.tacoId == idTaco):
          tacoYaRegistrado = True
          tacoPedidoRegistrado = pedidoTaco
          break
        
      if(tacoYaRegistrado):
        print("")
        print(f"{tacoPedidoRegistrado.taco.nombre} ya fue registrado")
        cantidadTaco = int(input("Digite la nueva cantidad deseada de tacos: "))
        
        for pedidoTaco in pedidoObj.pedidosTacos:
          if(pedidoTaco.taco.tacoId == idTaco):
            totalAnterior = pedidoTaco.cantidad * pedidoTaco.taco.precio
            pedidoObj.total -= totalAnterior
            pedidoTaco.cantidad = cantidadTaco 
            totalNuevo = pedidoTaco.cantidad * pedidoTaco.taco.precio
            pedidoObj.total += totalNuevo
            break  
      
      else:
        tacoEncontrado = False
        tacoEncontradoData = None
      
        # Existe el taco con ese id
        for taco in tacos:
          if(taco.tacoId == idTaco):
            tacoEncontrado = True
            tacoEncontradoData = taco
            break
        
        if(tacoEncontrado):
          cantidadTaco = int(input("Digite la cantidad deseada de tacos: "))
          pedidoObj.pedidosTacos.append(PedidoTaco(tacoEncontradoData, cantidadTaco))
          pedidoObj.total = pedidoObj.total + (cantidadTaco * tacoEncontradoData.precio)
          
        else:
          print("")
          print("El taco no se encontró")
          input("Presione una tecla para continuar...")
        