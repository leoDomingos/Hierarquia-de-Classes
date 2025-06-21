from typing import Any, Optional, Iterable, Iterator


from DoublyNode import DoublyNode
from LinearDataStructure import *

class DoublyLinkedList(LinearDataStructure):
    """Implementação de DoublyLinkedLIst"""
    
    def __init__(self, iterable: Optional[Iterable] = None):
        self._head: Optional[DoublyNode] = None
        self._tail: Optional[DoublyNode] = None
        self._size = 0
        
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)
    
    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def swap(self, index: int) -> None:
        """Troca dois nós adjacentes na lista, a partir do índice do primeiro."""
        if index < 0 or index >= self._size - 1:
            raise IndexError("Índice inválido ou último elemento")
        
        # Obter os nós a serem trocados
        node1 = self._get_node(index)
        node2 = node1.next
        
        # Caso especial: node1 é a cabeça da lista
        # Será que tem como generalizar?
        if node1 == self._head:
            self._head = node2
        else:
            node1.prev.next = node2
        
        # Atualizando os ponteiros
        node1.next = node2.next
        node2.prev = node1.prev
        
        node1.prev = node2
        node2.next = node1
        
        # Se existir um nó após os trocados
        if node1.next is not None:
            node1.next.prev = node1
        
        # Caso especial: node2 era o último elemento
        if node2 == self._tail:
            self._tail = node1
    
    def push(self, item: Any) -> None:
        """Insere no início (alias para insert_start)"""
        self.insert_start(item)
    
    def pop(self) -> Any:
        """Remove do início (alias para remove_start)"""
        return self.remove_start()
    
    def insert_start(self, item: Any) -> None:
        """Insere no início da lista"""
        new_node = DoublyNode(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1
    
    def insert_end(self, item: Any) -> None:
        """Insere no final da lista"""
        new_node = DoublyNode(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1
    
    def insert_at(self, index: int, item: Any) -> None:
        """Insere em posição específica"""
        if index == 0:
            self.insert_start(item)
        elif index == self._size:
            self.insert_end(item)
        else:
            self._validate_index(index)
            new_node = DoublyNode(item)
            current = self._get_node(index)
            
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self._size += 1
    
    def remove_start(self) -> Any:
        """Remove do início"""
        if self.is_empty():
            raise IndexError("Lista vazia")
        
        data = self._head.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return data
    
    def remove_end(self) -> Any:
        """Remove do final"""
        if self.is_empty():
            raise IndexError("Lista vazia")
        
        data = self._tail.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return data
    
    def remove_at(self, index: int) -> Any:
        """Remove de posição específica"""
        if index == 0:
            return self.remove_start()
        elif index == self._size - 1:
            return self.remove_end()
        
        self._validate_index(index)
        current = self._get_node(index)
        
        current.prev.next = current.next
        current.next.prev = current.prev
        self._size -= 1
        return current.data
    
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
        """Consulta posição sem remover"""
        return self._get_node(index).data
    
    def __iter__(self) -> Iterator:
        """Iteração normal"""
        current = self._head
        while current is not None:
            yield current.data
            current = current.next
    
    def __reversed__(self) -> Iterator:
        """Iteração reversa"""
        current = self._tail
        while current is not None:
            yield current.data
            current = current.prev
    
    def peek_at(self, index: int) -> Any:
        """Consulta posição sem remover"""
        return self._get_node(index).data  # Note o .data aqui

    def _get_node(self, index: int) -> DoublyNode:
        """Obtém o nó na posição especificada"""
        self._validate_index(index)
        
        if index < self._size // 2:
            # Percorre do início se estiver na primeira metade
            current = self._head
            for _ in range(index):
                current = current.next
        else:
            # Percorre do final se estiver na segunda metade
            current = self._tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        return current
    
    def insert_ordered(self, item: Any, key=None) -> None:
        """Insere um elemento na posição correta mantendo a lista ordenada."""
        if self._size == 0:
            self.insert_start(item)
            return
        
        # Decide a função de comparação
        if key is None:
            compare_func = lambda x: x
        else:
            compare_func = key
        
        new_value = compare_func(item)
        current = self._head
        
        # Encontra a posição correta para inserção
        while current is not None:
            current_value = compare_func(current.data)
            if new_value <= current_value:
                break
            current = current.next
        
        if current is None:
            # Insere no final
            self.insert_end(item)
        elif current == self._head:
            # Insere no início
            self.insert_start(item)
        else:
            # Insere no meio
            new_node = DoublyNode(item)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self._size += 1
    
    def _validate_index(self, index: int) -> None:
        """Valida se o índice é válido"""
        if index < 0 or index >= self._size:
            raise IndexError(f"Índice {index} inválido para lista de tamanho {self._size}")
    
    def __str__(self) -> str:
        """Representação em string"""
        items = [str(item) for item in self]
        return f"DoublyLinkedList([{', '.join(items)}])"
    
    def bubble_sort(self, key=None) -> None:
        """Ordena a lista usando o algoritmo bubble-sort com uma chave opcional."""
        if self._size <= 1:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self._head
            
            while current.next is not None:
                # Obter os valores para comparação
                data_current = key(current.data) if key else current.data
                data_next = key(current.next.data) if key else current.next.data
                
                if data_current > data_next:
                    # Troca os nós
                    if current == self._head:
                        self.swap(0)
                        current = self._head  # Atualiza a referência
                    else:
                        # Encontra o índice do nó atual para usar swap
                        idx = 0
                        temp = self._head
                        while temp != current:
                            temp = temp.next
                            idx += 1
                        self.swap(idx)
                        current = temp.prev  # Atualiza a referência
                    
                    swapped = True
                else:
                    current = current.next
    
    