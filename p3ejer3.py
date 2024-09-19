class ArbolBinario:
    
    def __init__(self, dato):
        """Inicializa un nodo del árbol binario."""
        self.dato = dato
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


class ContadorArbol:
    def __init__(self, arbol_binario):
        self.arbol_binario = arbol_binario

    def numeros_pares(self):
        pares = []
        self._inorder(self.arbol_binario, pares)
        return pares

    def _inorder(self, nodo, pares):
        if nodo is not None:
            self._inorder(nodo.hijo_izquierdo, pares)
            if nodo.dato % 2 == 0:
                pares.append(nodo.dato)
            self._inorder(nodo.hijo_derecho, pares)

    def numeros_pares_postorden(self):
        pares = []
        self._postorder(self.arbol_binario, pares)
        return pares

    def _postorder(self, nodo, pares):
        if nodo is not None:
            self._postorder(nodo.hijo_izquierdo, pares)
            self._postorder(nodo.hijo_derecho, pares)
            if nodo.dato % 2 == 0:
                pares.append(nodo.dato)
# Creamos un objeto de la clase ArbolBinario
arbol = ArbolBinario(5+1)

# Agregamos algunos valores al árbol
arbol.agregar_ordenado(3+1)
arbol.agregar_ordenado(7+1)
arbol.agregar_ordenado(2+1)
arbol.agregar_ordenado(4+1)
arbol.agregar_ordenado(6+1)
arbol.agregar_ordenado(8+1)

# Creamos un objeto de la clase ContadorArbol
contador = ContadorArbol(arbol)

# Imprimimos los números pares en orden
print("Números pares en orden:")
print(contador.numeros_pares())

# Imprimimos los números pares en postorden
print("Números pares en postorden:")
print(contador.numeros_pares_postorden())