from LinearDataStructure import *

class Array(LinearDataStructure):
    """Implementação de um array dinâmico com operador de indexação sobrecarregado"""
    
    def __init__(self, iterable: Optional[Iterable] = None, initial_capacity: int = 10):
        self._capacity = max(initial_capacity, 1)  # Capacidade mínima de 1, se não não faz sentido
        self._items = [None] * self._capacity
        self._size = 0
        
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)
    
    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, index: int) -> Any:
        """Operador [] para consulta (Rvalue)."""
        if index < 0 or index >= self._size:
            raise IndexError("Array index out of bounds")
        return self._items[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        """Operador [] para atribuição(lvalue)."""
        if index < 0 or index >= self._size:
            raise IndexError("Array index out of bounds")
        self._items[index] = value
    
    def _resize(self, new_capacity: int) -> None:
        """Redimensiona o array interno (só quando necessário)"""
        new_items = [None] * new_capacity
        for i in range(self._size):
            new_items[i] = self._items[i]
        self._items = new_items
        self._capacity = new_capacity
    
    def insert_start(self, item: Any) -> None:
        """Insere no início do array."""
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        
        for i in range(self._size, 0, -1):
            self._items[i] = self._items[i-1]
        
        self._items[0] = item
        self._size += 1
    
    def insert_end(self, item: Any) -> None:
        """Insere no final do array."""
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        
        self._items[self._size] = item
        self._size += 1
    
    def insert_at(self, index: int, item: Any) -> None:
        """Insere na posição especificada."""
        if index < 0 or index > self._size:
            raise IndexError("Array index out of bounds")
        
        if index == 0:
            self.insert_start(item)
        elif index == self._size:
            self.insert_end(item)
        else:
            if self._size == self._capacity:
                self._resize(self._capacity * 2)
            
            for i in range(self._size, index, -1):
                self._items[i] = self._items[i-1]
            
            self._items[index] = item
            self._size += 1
    
    def remove_start(self) -> Any:
        """Remove e retorna o elemento no início do array."""
        if self.is_empty():
            raise IndexError("Array underflow")
        
        item = self._items[0]
        for i in range(1, self._size):
            self._items[i-1] = self._items[i]
        
        self._size -= 1
        return item
    
    def remove_end(self) -> Any:
        """Remove e retorna o elemento no final do array."""
        if self.is_empty():
            raise IndexError("Array underflow")
        
        self._size -= 1
        return self._items[self._size]
    
    def remove_at(self, index: int) -> Any:
        """Remove e retorna o elemento na posição especificada."""
        if index < 0 or index >= self._size:
            raise IndexError("Array index out of bounds")
        
        if index == 0:
            return self.remove_start()
        elif index == self._size - 1:
            return self.remove_end()
        else:
            item = self._items[index]
            for i in range(index + 1, self._size):
                self._items[i-1] = self._items[i]
            
            self._size -= 1
            return item
    
    def peek_start(self) -> Any:
        """Retorna o elemento no início do array (sem remover)."""
        if self.is_empty():
            raise IndexError("Array underflow") # ou seria overflow
        return self._items[0]
    
    def peek_end(self) -> Any:
        """Retorna o elemento no final do array sem removê-lo."""
        if self.is_empty():
            raise IndexError("Array underflow") # talvez aqui seria overlfow? ver isos depois
        return self._items[self._size - 1]
    
    def peek_at(self, index: int) -> Any:
        """Retorna o elemento na posição especificada sem removê-lo."""
        if index < 0 or index >= self._size:
            raise IndexError("Array index out of bounds")
        return self._items[index]
    
    def __iter__(self) -> Iterator:
        """Retorna um iterador para o array."""
        for i in range(self._size):
            yield self._items[i]
    
    def __str__(self) -> str:
        """Retorna uma representação em string do array."""
        return f"Array([{', '.join(str(self._items[i]) for i in range(self._size))}], capacity={self._capacity})"