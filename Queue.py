from typing import Any, Optional, Iterable, Iterator, List
from datetime import datetime, timedelta
from LinearDataStructure import LinearDataStructure

class Prato:
    """prato do bandejão"""
    def __init__(self, nome: str, tempo_preparo: int):
        self.nome = nome
        self.tempo_preparo = tempo_preparo  # em minutos
    
    def __repr__(self):
        return f"Prato({self.nome}, {self.tempo_preparo}min)"

class Usuario:
    """usuário na fila do bandejão"""
    def __init__(self, id_usuario: int, nome: str):
        self.id = id_usuario
        self.nome = nome
        self.prato: Optional[Prato] = None
        self.hora_entrada: Optional[datetime] = None
        self.tempo_estimado: Optional[int] = None  # em minutos
        self.hora_retirada: Optional[datetime] = None
    
    def atualizar_tempo_estimado(self, posicao_fila: int, tempo_medio: int):
        """atualiza o tempo estimado baseado na posição e tempo médio"""
        self.tempo_estimado = (posicao_fila) * tempo_medio  # posicao_fila agora é 1-based
        if self.hora_entrada:
            self.hora_retirada = self.hora_entrada + timedelta(minutes=self.tempo_estimado)
    
    def __repr__(self):
        return f"Usuario({self.id}, {self.nome}, {self.tempo_estimado}min)"

class FilaBandejao(LinearDataStructure):
    """Implementação da fila do bandejão com controle de tempo"""
    
    def __init__(self, tempo_medio_atendimento: int = 2):
        super().__init__()  # Chama o construtor da classe pai
        self._items: List[Usuario] = []
        self.tempo_medio = tempo_medio_atendimento
        self.atraso_acumulado = 0
    
    def __len__(self) -> int:
        return len(self._items)
    
    def insert_start(self, item: Any) -> None:
        """Insere um elemento no início da fila"""
        # Implementação não usual para uma fila, mas necessária pela classe abstrata
        self._items.insert(0, item)
        self._atualizar_tempos()
    
    def insert_end(self, item: Any) -> None:
        """Insere um elemento no final da fila (enqueue)"""
        self._items.append(item)
        self._atualizar_tempos()
    
    def remove_start(self) -> Any:
        """Remove e retorna o elemento no início da fila (dequeue)"""
        if self.is_empty():
            raise IndexError("Fila vazia")
        item = self._items.pop(0)
        self._atualizar_tempos()
        return item
    
    def remove_end(self) -> Any:
        """Remove e retorna o elemento no final da fila"""
        # Implementação não usual para uma fila, mas necessária pela classe abstrata
        if self.is_empty():
            raise IndexError("Fila vazia")
        item = self._items.pop()
        self._atualizar_tempos()
        return item
    
    def enqueue(self, usuario: Usuario, prato: Prato) -> None:
        """Adiciona um usuário na fila com um prato"""
        usuario.prato = prato
        usuario.hora_entrada = datetime.now()
        # Tempo total é tempo médio + tempo preparo prato + atraso acumulado
        tempo_total = self.tempo_medio + prato.tempo_preparo + self.atraso_acumulado
        usuario.atualizar_tempo_estimado(len(self._items), tempo_total)
        self.insert_end(usuario)
    
    def dequeue(self) -> Usuario:
        """Remove e retorna o próximo usuário da fila"""
        return self.remove_start()  # Usa remove_start para remover do início
    
    def desistencia(self, id_usuario: int) -> bool:
        """Remove um usuário da fila por desistência"""
        for i, usuario in enumerate(self._items):
            if usuario.id == id_usuario:
                self._items.pop(i)
                self._atualizar_tempos()
                return True
        return False
    
    def _atualizar_tempos(self) -> None:
        """Atualiza os tempos estimados para todos os usuários na fila"""
        for i, usuario in enumerate(self._items):
            usuario.atualizar_tempo_estimado(i + 1, self.tempo_medio + self.atraso_acumulado)  # i+1 para tornar 1-based
    
    def registrar_atraso(self, minutos: int) -> None:
        """Registra um atraso no atendimento"""
        self.atraso_acumulado += minutos
        self._atualizar_tempos()
    
    def registrar_adiantamento(self, minutos: int) -> None:
        """Registra um adiantamento no atendimento"""
        self.atraso_acumulado = max(0, self.atraso_acumulado - minutos)
        self._atualizar_tempos()
    
    def tempo_espera_atual(self) -> int:
        """Retorna o tempo de espera estimado para novos usuários"""
        return len(self._items) * (self.tempo_medio + self.atraso_acumulado)
    
    def peek_start(self) -> Usuario:
        """Retorna o próximo usuário sem remover"""
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self._items[0]
    
    def peek_end(self) -> Usuario:
        """Retorna o último usuário sem remover"""
        if self.is_empty():
            raise IndexError("Fila vazia")
        return self._items[-1]
    
    def __iter__(self) -> Iterator[Usuario]:
        """Iterador para a fila"""
        return iter(self._items)
    
    def get_usuario(self, id_usuario: int) -> Optional[Usuario]:
        """Obtém um usuário específico da fila"""
        for usuario in self._items:
            if usuario.id == id_usuario:
                return usuario
        return None