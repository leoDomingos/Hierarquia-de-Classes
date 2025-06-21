from typing import Any, Optional, Iterable, Iterator

class Node:    
    def __init__(self, data: Any):
        self.data = data  # Padronizado sem underscore
        self.next = None
    
    def __str__(self):
        return str(self.data)