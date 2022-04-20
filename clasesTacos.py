class Taco:
  def __init__(self, tacoId, nombre, precio):
    self.nombre = nombre
    self.tacoId = tacoId
    self.precio = precio
    
class Pedido:
  def __init__(self, pedidoId, total, pedidosTacos):
    self.pedidoId = pedidoId
    self.total = total
    self.pedidosTacos = pedidosTacos
    
class PedidoTaco:
  def __init__(self, taco, cantidad):
    self.taco = taco
    self.cantidad = cantidad