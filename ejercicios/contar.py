# Define una clase Node que representa un nodo en un árbol binario. Cada nodo tiene un valor, 
# así como referencias a sus nodos hijos izquierdo y derecho.

# Define una clase BinaryTree que representa el árbol binario en sí. Tiene un atributo root que apunta al nodo raíz del árbol.

# La clase BinaryTree tiene un método insert para insertar un nuevo valor en el árbol. Si el árbol está vacío, crea un 
# nuevo nodo y lo establece como la raíz. De lo contrario, utiliza un método auxiliar _insert_recursive para insertar el 
# valor en el lugar adecuado del árbol de manera recursiva.

# La clase BinaryTree también tiene un método inorder_traversal que realiza un recorrido en orden del árbol (de menor a mayor), 
# imprimiendo los valores de los nodos en orden ascendente.

 
# Definir la clase Node
class Node:
    #Crear el constructor para Crear el nodo con un lado izquierdo y derecho
    #también toma un valor(key)
    def __init__(self,key):
        self.right = None
        self.left = None
        self.key = key
        pass
# Definir la clase BinaryTree
class BinaryTree:
    #Crear el constructor para Crear el árbol con una raíz
    def __init__(self):
        self.root = None
        pass
    #Crear el método para insertar nodos
    def insert(self, key):
        #Si el nodo actual no tiene ningún valor, 
        #define en el actual el valor actual
        if self.root is None:
            self.root = Node(key)
        else:
        #De lo contrario, llama al método _insert_recursive     
            self._insert_recursive(self.root, key)  
        pass
    #Crear el método para discriminar nodos 
    def _insert_recursive(self, _current_node, key):
        #Si el valor que se quiere pasar ahora es inferior al del
        #nodo actual, se almacenará a la izquierda
        if key < _current_node.key:
            if _current_node.left is None:
                _current_node.left = Node(key)
                pass
            else:
                self._insert_recursive(_current_node.left, key)
            #Si el nodo actual es None es porque se va a insertar uno nuevo a la izquierda
        elif key > _current_node.key:
            if _current_node.right is None:
                _current_node.right = Node(key)
                pass
            else:
                self._insert_recursive(_current_node.right, key)
            
        
    def _count(self,Node):
        if Node is not None:
            self._count(Node.left)
            print(Node.key, end=" ")
            self._count(Node.right)
        
            
             
tree = BinaryTree()
   
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)   
# Recorrido en orden (de menor a mayor)
print("Recorrido en orden:")
tree._count(tree.root)
        