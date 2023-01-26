from node import Node

class QueueDequeueException(Exception):
    ...

# Classe que define uma Fila
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._count = 0

    # inserir na fila
    def enqueue(self, value):
        node = Node(value)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._count = self._count + 1

    # remover da fila
    def dequeue(self):
        if self._count > 0:
            value = self.first.value
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._count = self._count - 1
            return value
        raise QueueDequeueException('Empty Queue')
    
    # verifica se a fila esta vazia
    def is_empty(self):
        return self._count < 1

    # retorna o tamanho da fila 
    def __len__(self):
        return self._count

    # retorna a representação visual da fila 
    def __str__(self):
        r = ""
        fila = self.first
        while(fila):
            r = r + str(fila.value) + " -> "
            fila = fila.next
        return r[:-4]


if __name__ == "__main__":
    queue = Queue()

    a = print(queue)

    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()

    print(queue)