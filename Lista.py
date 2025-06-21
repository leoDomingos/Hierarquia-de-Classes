from LinearDataStructure import *
from Array import *


class Lista(LinearDataStructure):
    """Implementação de Lista usando a classe Array"""
    
    def __init__(self, iterable: Optional[Iterable] = None):
        self._dados = Array()  # Usa nossa classe Array como armazenamento interno
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)
    
    def __len__(self) -> int:
        return len(self._dados)
    
    def push(self, item: Any) -> None:
        """Insere um item no início da lista (alias pra insert_start)."""
        self.insert_start(item)
    
    def pop(self) -> Any:
        """Remove e retorna o item do início da lista (alias paraa remove_start)."""
        return self.remove_start()
    
    def insert_start(self, item: Any) -> None:
        """Insere um item no início da lista."""
        self._dados.insert_start(item)
    
    def insert_end(self, item: Any) -> None:
        """Insere um item no final da lista."""
        self._dados.insert_end(item)
    
    def insert_at(self, index: int, item: Any) -> None:
        """Insere um item na posição especificada."""
        self._dados.insert_at(index, item)
    
    def remove_start(self) -> Any:
        """Remove e retorna o item do início da lista."""
        return self._dados.remove_start()
    
    def remove_end(self) -> Any:
        """Remove e retorna o item do final da lista."""
        return self._dados.remove_end()
    
    def remove_at(self, index: int) -> Any:
        """Remove e retorna o item da posição especificada."""
        return self._dados.remove_at(index)
    
    def peek_start(self) -> Any:
        """Retorna o item do início da lista sem remover."""
        return self._dados.peek_start()
    
    def peek_end(self) -> Any:
        """Retorna o item do final da lista sem remover."""
        return self._dados.peek_end()
    
    def peek_at(self, index: int) -> Any:
        """Retorna o item da posição especificada sem remover."""
        return self._dados.peek_at(index)
    
    def __iter__(self) -> Iterator:
        """Retorna um iterador para a lista."""
        return iter(self._dados)
    
    def __str__(self) -> str:
        """Retorna uma representação em string da lista."""
        return f"Lista([{', '.join(str(item) for item in self._dados)}])"