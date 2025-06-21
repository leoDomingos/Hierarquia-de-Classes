from abc import ABC, abstractmethod
from typing import Any, Optional, Iterable, Iterator

class LinearDataStructure(ABC):
    """Classe pro resto das estruturas de dados"""
    
    def __init__(self, iterable: Optional[Iterable] = None):
        """Inicializa a estrutura de dados, opcionalmente com elementos de um iterável."""
        if iterable is not None:
            for item in iterable:
                self.insert_end(item)
    
    @abstractmethod
    def __len__(self) -> int:
        """Retorna o número de elementos na estrutura."""
        pass
    
    def is_empty(self) -> bool:
        """Verifica se a estrutura está vazia."""
        return len(self) == 0
    
    def is_full(self) -> bool:
        """Verifica se a estrutura está cheia (sempre False para estruturas sem tamanho fixo)."""
        return False
    
    @abstractmethod
    def insert_start(self, item: Any) -> None:
        """Insere um elemento no início da estrutura."""
        pass
    
    @abstractmethod
    def insert_end(self, item: Any) -> None:
        """Insere um elemento no final da estrutura."""
        pass
    
    def insert_at(self, index: int, item: Any) -> None:
        """Insere um elemento na posição especificada."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def insert_before(self, key: Any, item: Any) -> None:
        """Insere um elemento antes do elemento com a chave especificada."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def insert_after(self, key: Any, item: Any) -> None:
        """Insere um elemento depois do elemento com a chave especificada."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    @abstractmethod
    def remove_start(self) -> Any:
        """Remove e retorna o elemento no início da estrutura."""
        pass
    
    @abstractmethod
    def remove_end(self) -> Any:
        """Remove e retorna o elemento no final da estrutura."""
        pass
    
    def remove_at(self, index: int) -> Any:
        """Remove e retorna o elemento na posição especificada."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def remove_key(self, key: Any) -> None:
        """Remove o elemento com a chave especificada."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def peek_start(self) -> Any:
        """Retorna o elemento no início da estrutura sem removê-lo."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def peek_end(self) -> Any:
        """Retorna o elemento no final da estrutura sem removê-lo."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def peek_at(self, index: int) -> Any:
        """Retorna o elemento na posição especificada sem removê-lo."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def peek_key(self, key: Any) -> Any:
        """Retorna o elemento com a chave especificada sem removê-lo."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def peek_next(self, key: Any) -> Any:
        """Retorna o próximo elemento com a mesma chave após o último encontrado."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def __iter__(self) -> Iterator:
        """Retorna um iterador para a estrutura."""
        raise NotImplementedError("Esta operação não é suportada por esta estrutura")
    
    def __str__(self) -> str:
        """Retorna uma representação em string da estrutura."""
        return f"{self.__class__.__name__}([{', '.join(str(item) for item in self)}])"
