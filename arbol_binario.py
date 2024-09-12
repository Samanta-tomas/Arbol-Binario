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
        
    def obtener_hijo_izquierdo(self):
        return self.hijo_izquierdo
        
    def agregar_hijo_izquierdo(self, hijo):
        """Agrega un nuevo nodo hijo izquierdo."""
        self.hijo_izquierdo = hijo
         
    def obtener_hijo_derecho(self):
            return self.hijo_derecho
  
    def agregar_hijo_derecho(self, hijo):
        if self.hijo_derecho is None:
            self.hijo_derecho = hijo
        else:
            return not None
        
    def eliminar_hijo_izquierdo(self):
        self.hijo_izquierdo = None

    def eliminar_hijo_derecho(self):
        self.hijo_derecho = None
        
    def esta_vacio(self):
        """Indica si el árbol está vacío."""
        return self.dato is None
    
    def es_hoja(self):
        """Indica si el nodo es una hoja (no tiene hijos)."""
        return self.hijo_izquierdo is None and self.hijo_derecho is None
    
    def tiene_hijo_izquierdo(self):
        """Devuelve un booleano indicando si el árbol tiene hijo izquierdo."""
        return self.hijo_izquierdo is not None

    def tiene_hijo_derecho(self):
        """Devuelve un booleano indicando si el árbol tiene hijo derecho."""
        return self.hijo_derecho is not None
    
    def contar_hojas(self):
        if self.es_hoja():
            return 1
        else: 
            count = 0
            if self.tiene_hijo_izquierdo():
                count += self.hijo_izquierdo.contar_hojas()
            if self.tiene_hijo_derecho():
                count += self.hijo_derecho.contar_hojas()
            return count
            
    def espejo(self): 
        nuevo_arbol = ArbolBinario(self.dato)
        if self.tiene_hijo_izquierdo():
            nuevo_arbol.agregar_hijo_derecho(self.hijo_izquierdo.espejo())
        if self.tiene_hijo_derecho():
            nuevo_arbol.agregar_hijo_izquierdo(self.hijo_derecho.espejo())
        return nuevo_arbol
    
    #def imprimir_entre_niveles(self, n, m): ...no lo entiendo
        
           
# Creamos un árbol binario con el dato 5 (nodo raíz)
arbol = ArbolBinario(5)
valores = [9,8,3,2,4]
print(valores)

for valor in valores:
    arbol.agregar_ordenado(valor)
    
arbol.imprimir_in_orden()
arbol.espejo() #no lo toma

print()
print()

print("'Hijo izquiergo, hijo derecho agregados de a uno'")

arbol.agregar_hijo_izquierdo(8) #Cuál es la lógica de agregar derecho o izquierdo si el arbol lo ordena por comparación??
arbol.agregar_hijo_derecho(20)  #??
print(f"Tiene hijo izquierdo:", arbol.tiene_hijo_izquierdo())  
print(f"Tiene hijo derecho:", arbol.tiene_hijo_derecho())  

arbol.eliminar_hijo_derecho()

print()

print(f"Tiene hijo izquierdo:", arbol.tiene_hijo_izquierdo())  
print(f"Tiene hijo derecho:", arbol.tiene_hijo_derecho()) 

print(f"Es hoja:", arbol.es_hoja()) #??
    







"""# Agregamos un hijo izquierdo con el dato 3 (llamo a los métodos utilizando las instancias (objeto))
arbol.agregar_hijo_izquierdo(ArbolBinario(3))
# Agregamos un hijo derecho con el dato 8
arbol.agregar_hijo_derecho(ArbolBinario(8))

# Verificamos si el árbol tiene hijos izquierdo y derecho
print(f"Tiene hijo izquierdo:", arbol.tiene_hijo_izquierdo())  # True
print(f"Tiene hijo derecho:", arbol.tiene_hijo_derecho())  # True

# Eliminamos el hijo izquierdo
arbol.eliminar_hijo_izquierdo()

# Verificamos si el árbol tiene hijos izquierdo y derecho
print(f"Tiene hijo izquierdo:", arbol.tiene_hijo_izquierdo())  # False
print(f"Tiene hijo derecho:", arbol.tiene_hijo_derecho())  # True"""