from LinkedList import LinkedList
from Node import Node
from typing import Any, Optional, Iterable, Iterator

class CircularLinkedList(LinkedList):
    """Implementação de lista encadeada circular"""
    
    def __init__(self, max_size: int, iterable: Optional[Iterable] = None):
        self._max_size = max_size
        self._size = 0
        self._head = None
        self._tail = None
        
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)
    
    def is_full(self) -> bool:
        """Verifica se a lista está cheia """
        return self._size >= self._max_size
    
    def insert_end(self, item: Any) -> None: # (O(1)) eu acho
        """Insere no final"""
        if self.is_full():
            raise OverflowError("Lista circular está cheia")
        

        # pq isso nao funciona?????
        # new_node = Node(item)
        # if self.is_empty():
        #     print(new_node)
        #     new_node.next = self._head  # Aponta para o início
        #     self._head = new_node
        #     self._tail = new_node
        #     new_node.next = new_node  # Circularidade
        # else:
        #     print(new_node)
        #     new_node.next = new_node  # Circularidade
        #     self._tail.next = new_node
        #     self._tail = new_node



        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            new_node.next = new_node  # Circularidade
        else:
            new_node.next = self._head  # Aponta para o início
            self._tail.next = new_node
            self._tail = new_node
        
        self._size += 1
    
    def insert_start(self, item: Any) -> None: # (O(1)) tbm
        """Insere no início."""
        if self.is_full():
            raise OverflowError("Lista circular está cheia!!")
        
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            new_node.next = new_node  # Circularidade
        else:
            new_node.next = self._head
            self._tail.next = new_node  # Atualiza o último nó para apontar para o novo início
            self._head = new_node
        
        self._size += 1
    
    def remove_start(self) -> Any:
        """Remove do início"""
        if self.is_empty():
            raise IndexError("Lista vazia.")
        
        data = self._head.data
        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._tail.next = self._head  # Mantém a circularidade
        
        self._size -= 1
        return data
    
    def remove_end(self) -> Any:
        """Remove do final (O(n))."""
        if self.is_empty():
            raise IndexError("Lista vazia")
        
        if self._size == 1:
            return self.remove_start()
        
        # Encontra o nó anterior ao tail
        prev_node = self._head
        while prev_node.next != self._tail:
            prev_node = prev_node.next
        
        data = self._tail.data
        prev_node.next = self._head  # Circularidade
        self._tail = prev_node
        self._size -= 1
        return data
    
    def __iter__(self) -> Iterator:
        """Iterador seguro para lista circular (não infinito)."""
        if self.is_empty():
            return
        
        current = self._head
        count = 0
        while count < self._size:
            yield current.data
            current = current.next
            count += 1
    
    def _get_node(self, index: int) -> Node:
        """Obtém o nó na posição especificada (O(n."""
        if index < 0 or index >= self._size:
            raise IndexError("Índice fora dos limites")
        
        current = self._head
        for _ in range(index):
            current = current.next
        return current
    
    def swap(self, index1: int, index2: int) -> None:
        """Troca dois nós consecutivos (setup pro bubble sort)."""
        if index1 < 0 or index2 < 0 or index1 >= self._size or index2 >= self._size:
            raise IndexError("Índices fora dos limites")
        
        if abs(index1 - index2) != 1:
            raise ValueError("Os índices devem ser consecutivos")
        
        if index1 > index2:
            index1, index2 = index2, index1  # Garante index1 < index2
        
        # Casos especiais: troca envolvendo head ou tail
        if index1 == 0 and index2 == 1:
            node1 = self._head
            node2 = node1.next
            node1.next = node2.next
            node2.next = node1
            self._head = node2
            if self._size == 2:
                self._tail = node1
            self._tail.next = self._head
            return
        
        if index2 == self._size - 1:
            node1 = self._get_node(index1)
            node2 = node1.next
            node1.next = node2.next
            node2.next = node1
            if index1 == 0:
                self._head = node2
            else:
                prev_node = self._get_node(index1 - 1)
                prev_node.next = node2
            self._tail = node1
            self._tail.next = self._head
            return
        
        # Caso geral
        prev_node = self._get_node(index1 - 1)
        node1 = prev_node.next
        node2 = node1.next
        node1.next = node2.next
        node2.next = node1
        prev_node.next = node2
    
    def sort(self) -> None:
        """Ordena a lista usando bubble sort."""
        if self._size <= 1:
            return
        
        swapped = True
        while swapped:
            swapped = False
            for i in range(self._size - 1):
                node1 = self._get_node(i)
                node2 = node1.next
                if node1.data > node2.data:
                    self.swap(i, i + 1)
                    swapped = True