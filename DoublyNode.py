from Node import *

class DoublyNode:
    """Nó pra doublylinkedlist"""
    def __init__(self, data: Any):
        self.data = data
        self.prev: Optional[DoublyNode] = None
        self.next: Optional[DoublyNode] = None