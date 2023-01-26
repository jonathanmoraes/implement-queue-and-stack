from node import Node


class StackPopException(Exception):
    ...

class Stack:
    def __init__(self):
        self.top = None
        self._count = 0

    # insere um elemento na pilha
    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._count += 1

    # remove o elemento do topo da pilha
    def pop(self):
        if self._count > 0:
            node = self.top
            self.top = self.top.next
            self._count -= 1
            return node.value
        raise StackPopException('Empty Stack')

    # retorna o tamanho da pilha
    def __len__(self):
        return self._count
    
    # verifica se a pilha esta vazia
    def is_empty(self) -> bool:
        return self._count < 1

    def __str__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.value) + " -> "
            pointer = pointer.next
        return r[:-4]

if __name__ == "__main__":
    stack = Stack()

    print(stack)

    stack.push(3)
    stack.push(1)
    stack.push(2)
    stack.pop()

    print(stack)