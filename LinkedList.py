from LinearDataStructure import *
from Node import *

class LinkedList(LinearDataStructure):
    """Implementação de lista encadeada simples."""
    
    def __init__(self, iterable: Optional[Iterable] = None):
        self._head = None
        self._tail = None
        self._size = 0
        
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)
    
    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def insert_start(self, item: Any) -> None:
        """Insere no início"""
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node
        
        if self._tail is None:
            self._tail = new_node
        
        self._size += 1
    
    def insert_end(self, item: Any) -> None:
        """Insere no final"""
        new_node = Node(item)
        
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        
        self._tail = new_node
        self._size += 1
    
    def _get_node(self, index: int) -> Node:
        """Obtém o nó na posição especificada"""
        if index < 0 or index >= self._size:
            raise IndexError("Índice fora dos limites")
        
        current = self._head
        for _ in range(index):
            current = current.next
        return current
    
    def insert_at(self, index: int, item: Any) -> None:
        """Insere em posição específica"""
        if index == 0:
            self.insert_start(item)
        elif index == self._size:
            self.insert_end(item)
        else:
            prev_node = self._get_node(index - 1)
            new_node = Node(item)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self._size += 1
    
    def remove_start(self) -> Any:
        """Remove do início"""
        if self.is_empty():
            raise IndexError("Lista vazia")
        
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        
        if self.is_empty():
            self._tail = None
            
        return data
    
    def remove_end(self) -> Any:
        """Remove do final"""
        if self.is_empty():
            raise IndexError("Lista vazia")
        
        if self._size == 1:
            return self.remove_start()
        
        prev_node = self._get_node(self._size - 2)
        data = self._tail.data
        prev_node.next = None
        self._tail = prev_node
        self._size -= 1
        return data
    
    def remove_at(self, index: int) -> Any:
        """Remove de posição específica"""
        if index == 0:
            return self.remove_start()
        elif index == self._size - 1:
            return self.remove_end()
        
        prev_node = self._get_node(index - 1)
        data = prev_node.next.data
        prev_node.next = prev_node.next.next
        self._size -= 1
        return data
    
    def peek_start(self) -> Any:
        """Consulta início sem remover"""
        if self.is_empty():
            raise IndexError("Lista vazia")
        return self._head.data
    
    def peek_end(self) -> Any:
        """Consulta final sem remover"""
        if self.is_empty():
            raise IndexError("Lista vazia")
        return self._tail.data
    
    def peek_at(self, index: int) -> Any:
        """Consulta por índice sem remover"""
        return self._get_node(index).data
    
    def __iter__(self) -> Iterator:
        current = self._head
        while current is not None:
            yield current.data
            current = current.next
    
    def __str__(self) -> str:
        """Representação em string"""
        items = []
        current = self._head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return f"LinkedList([{', '.join(items)}])"