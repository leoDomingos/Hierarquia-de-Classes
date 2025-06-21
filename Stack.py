from LinearDataStructure import *
from LinkedList import *

class Stack(LinearDataStructure):
    """Implementação de uma pilha usando lista"""
    
    def __init__(self, iterable: Optional[Iterable] = None):
        self._items = LinkedList()  # Usando lista encadeada internamente
        # Precisamos inserir os elementos na ordem inversa para manter o LIFO
        if iterable is not None:
            for item in reversed(list(iterable)):
                self._items.insert_start(item)
    
    def __len__(self) -> int:
        return len(self._items)
    
    def push(self, item: Any) -> None:
        """Adiciona um elemento no topo da pilha."""
        self._items.insert_start(item)
    
    def pop(self) -> Any:
        """Remove e retorna o elemento do topo da pilha."""
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._items.remove_start()
    
    # Implementações dos métodos abstratos
    def insert_start(self, item: Any) -> None:
        """Insere um elemento no topo da pilha (push)."""
        self.push(item)
    
    def insert_end(self, item: Any) -> None:
        """Insere um elemento na base da pilha."""
        self._items.insert_end(item)
    
    def remove_start(self) -> Any:
        """Remove e retorna o elemento do topo da pilha (pop)."""
        return self.pop()
    
    def remove_end(self) -> Any:
        """Remove e retorna o elemento da base da pilha."""
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._items.remove_end()
    
    def peek_start(self) -> Any:
        """Retorna o elemento no topo da pilha sem removê-lo."""
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._items.peek_start()
    
    def peek_end(self) -> Any:
        """Retorna o elemento na base da pilha sem removê-lo."""
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._items.peek_end()
    
    def __iter__(self) -> Iterator:
        """Retorna um iterador para a pilha (do topo para a base)."""
        # Precisamos inverter a ordem pois a LinkedList itera do início ao fim
        # e queremos iterar do topo (início) para a base (fim)
        return iter(self._items)
    
    def __str__(self) -> str:
        """Retorna uma representação em string da pilha (topo primeiro)."""
        items = list(self._items)  # Converte a LinkedList para lista
        return f"Stack([{', '.join(str(item) for item in items)}])"