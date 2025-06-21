from CircularLinkedList import CircularLinkedList
from typing import List, Tuple

class FiguraGeometrica:
    """Classe que representa uma figura geométrica plana fechada."""

    def __init__(self, max_vertices: int, vertices: List[Tuple[float, float]] = None):
        """
        Inicializa a figura com um número máximo de vértices.
        
        Args:
            max_vertices: Número máximo de vértices da figura
            vertices: Lista opcional de vértices iniciais (x, y).
        """
        self._vertices = CircularLinkedList(max_size=max_vertices)
        if vertices is not None:
            for vertice in vertices:
                self.adicionar_vertice(vertice)

    def adicionar_vertice(self, vertice: Tuple[float, float]) -> None:
        """
        Adiciona um vértice à figura, garantindo que não haja linhas cruzadas.
        
        Args:
            vertice: Tupla (x, y) representando o vértice a ser adicionado.
        
        Raises:
            ValueError: Se a adição do vértice causar linhas cruzadas.
        """
        if self._vertices.is_full():
            raise OverflowError("Número máximo de vértices atingido")
        
        if len(self._vertices) >= 3:
            if self._ha_linhas_cruzadas(vertice):
                raise ValueError("A adição deste vértice causaria linhas cruzadas")
        
        self._vertices.insert_end(vertice)

    def _ha_linhas_cruzadas(self, novo_vertice: Tuple[float, float]) -> bool:
        """
        Verifica se a adição de um novo vértice causa linhas cruzadas.
        
        Args:
            novo_vertice: Tupla (x, y) representando o novo vértice.
        
        Returns:
            True se houver linhas cruzadas, False caso contrário.
        """
        vertices = list(self._vertices)
        if len(vertices) < 3:
            return False  # Não pode haver cruzamento com menos de 3 vértices
        
        # Adiciona o novo vértice temporariamente para verificação
        vertices.append(novo_vertice)
        n = len(vertices)
        
        # Verifica apenas o último segmento com os segmentos existentes
        for i in range(n - 3):
            if self._segmentos_se_cruzam(
                vertices[i], vertices[i + 1],
                vertices[-2], vertices[-1]
            ):
                return True
        
        # Verifica se o último segmento cruza com o segmento que fecha a figura
        if n >= 4:
            if self._segmentos_se_cruzam(
                vertices[-3], vertices[-2],
                vertices[-1], vertices[0]
            ):
                return True
        
        return False

    @staticmethod
    def _segmentos_se_cruzam( 
        a: Tuple[float, float], b: Tuple[float, float],
        c: Tuple[float, float], d: Tuple[float, float]
    ) -> bool:
        """
        Verifica se dois segmentos de linha AB e CD se cruzam.
        
        Args:
            a, b: Pontos do primeiro segmento (AB).
            c, d: Pontos do segundo segmento (CD).
        
        Returns:
            True se os segmentos se cruzam, False caso contrário.
        """
        def orientacao(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) # WTF?????????????
            if val == 0:
                return 0  # Colinear
            return 1 if val > 0 else 2  # Horário ou anti-horário

        def no_segmento(p, q, r):
            if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]): # ?????
                return True
            return False

        o1 = orientacao(a, b, c)
        o2 = orientacao(a, b, d)
        o3 = orientacao(c, d, a)
        o4 = orientacao(c, d, b)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and no_segmento(a, c, b):
            return True
        if o2 == 0 and no_segmento(a, d, b):
            return True
        if o3 == 0 and no_segmento(c, a, d):
            return True
        if o4 == 0 and no_segmento(c, b, d):
            return True

        return False

    def __str__(self) -> str:
        """Retorna uma representação em string da figura."""
        vertices = list(self._vertices)
        return f"FiguraGeometrica({vertices})"