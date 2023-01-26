# Nó para alocação da fila e da pilha 
from typing import Any  

class Node:
    def __init__(self, Value):
        self.value = Value
        self.next = None