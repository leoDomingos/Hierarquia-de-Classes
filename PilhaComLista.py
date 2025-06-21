from Lista import *

class PilhaComLista:
    """Implementação de Pilha com a Lista"""
    
    def __init__(self, iterable: Optional[Iterable] = None):
        self._dados = Lista()  # Usa nossa classe Lista como armazenamento interno
        if iterable is not None:
            for item in reversed(list(iterable)):
                self.push(item)
    
    def __len__(self) -> int:
        return len(self._dados)
    
    def push(self, item: Any) -> None:
        """Empilha um item no topo da pilha."""
        self._dados.insert_start(item)
    
    def pop(self) -> Any:
        """Desempilha e retorna o item do topo da pilha."""
        if len(self) == 0:
            raise IndexError("Pilha vazia")
        return self._dados.remove_start()
    
    def top(self) -> Any:
        """Retorna o item do topo da pilha sem remover."""
        if len(self) == 0:
            raise IndexError("Pilha vazia")
        return self._dados.peek_start()
    
    def is_empty(self) -> bool:
        """Verifica se a pilha está vazia."""
        return len(self) == 0
    
    def __str__(self) -> str:
        """Retorna uma representação em string da pilha."""
        return f"Pilha([{', '.join(str(item) for item in self._dados)}])"