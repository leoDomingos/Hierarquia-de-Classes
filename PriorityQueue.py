

# Exemplo de fila de prioridades
class PriorityItem:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
    
    def __repr__(self):
        return f"{self.value} (prio: {self.priority})"