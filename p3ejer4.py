class ArbolBinario:
    
    def __init__(self, dato, retardo=0):
        """Inicializa un nodo del árbol binario."""
        self.dato = dato
        self.retardo = retardo
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        
    def imprimir_in_orden(self):
        """Imprime el árbol en inorden usando recursividad."""
        if self.hijo_izquierdo:
            self.hijo_izquierdo.imprimir_in_orden()
        print(self.dato, end=' ')
        if self.hijo_derecho:
            self.hijo_derecho.imprimir_in_orden()

    def imprimir_post_orden(self):
        """Imprime el árbol en postorden usando recursividad."""
        if self.hijo_izquierdo:
            self.hijo_izquierdo.imprimir_post_orden()
        if self.hijo_derecho:
            self.hijo_derecho.imprimir_post_orden()
        print(self.dato, end=' ')

    def agregar_ordenado(self, valor):
      """Agrega un valor al árbol binario de manera ordenada usando recursividad."""
      if valor < self.dato:
          if self.hijo_izquierdo is None:
              self.hijo_izquierdo = ArbolBinario(valor)
          else:
              self.hijo_izquierdo.agregar_ordenado(valor)
      else:
          if self.hijo_derecho is None:
              self.hijo_derecho = ArbolBinario(valor)
          else:
              self.hijo_derecho.agregar_ordenado(valor)

class RedBinaria(ArbolBinario):

    def __init__(self, dato, retardo_ms=0):
        super().__init__(dato, retardo_ms)

    def retardo_maximo(self):
        """Calcula el mayor retardo posible en un mensaje desde la raíz hasta las hojas."""
        return self._retardo_maximo(self)

    def _retardo_maximo(self, nodo):
        if nodo is None:
            return 0
        if nodo.hijo_izquierdo is None and nodo.hijo_derecho is None:
            return nodo.retardo
        retardo_izquierdo = self._retardo_maximo(nodo.hijo_izquierdo)
        retardo_derecho = self._retardo_maximo(nodo.hijo_derecho)
        return nodo.retardo + max(retardo_izquierdo, retardo_derecho)

    
# Creamos un objeto de la clase RedBinaria
red = RedBinaria(5, 1)

# Agregamos nodos con retardos de reenvío
red.hijo_izquierdo = RedBinaria(3, 2)
red.hijo_derecho = RedBinaria(7, 3)
red.hijo_izquierdo.hijo_izquierdo = RedBinaria(2, 1)
red.hijo_izquierdo.hijo_derecho = RedBinaria(4, 2)
red.hijo_derecho.hijo_izquierdo = RedBinaria(6, 1)
red.hijo_derecho.hijo_derecho = RedBinaria(8, 3)

# Calculamos el mayor retardo posible
print("Mayor retardo posible:", red.retardo_maximo())

