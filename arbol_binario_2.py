class ArbolBinario:
    
    def __init__(self, dato):
        """Inicializa un nodo del árbol binario."""
        self.dato = dato
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        
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
        
    def esta_vacio(self):
        """Indica si el árbol está vacío."""
        return self.dato is None
    
    def es_hoja(self):
        """Indica si el nodo es una hoja (no tiene hijos)."""
        return self.hijo_izquierdo is None and self.hijo_derecho is None

                    
arbol = ArbolBinario(30)
valores = [22, 5, 8, 44, 50, 12, 31, 60, 35, 9]
for valor in valores:
    arbol.agregar_ordenado(valor)
    
arbol.imprimir_in_orden()
print()
arbol.imprimir_post_orden()
print()
print(arbol.es_hoja())







    

    