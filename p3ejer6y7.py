class ArbolBinario:
    
    def __init__(self, dato):
        """Inicializa un nodo del árbol binario."""
        self.dato = dato
        self.hijo_izquierdo = None
        self.hijo_derecho = None

    def agregar(self, prducto):

        if prducto < self.dato:
          if self.hijo_izquierdo is None:
              self.hijo_izquierdo = ArbolBinario(prducto)
          else:
              self.hijo_izquierdo.agregar(prducto)
        else:
          if self.hijo_derecho is None:
              self.hijo_derecho = ArbolBinario(prducto)
          else:
              self.hijo_derecho.agregar(prducto)

class Producto:

    def __init__(self, nombre, codigo_producto, cantidad_productos, precio_unidad):
        self.nombre = nombre
        self.codigo_producto = codigo_producto
        self.cantidad_productos = cantidad_productos
        self.precio_unidad = precio_unidad

class Ferreteria:

    def __init__(self):
        for total_productos in Producto:
            if total_productos is None:
                return 0
            else:
                total_productos = total_productos +1
                return total_productos
            
    