##

# Aluno: Leonardo Domingos
# DRE: 120168324
#
#
# Falta:
# * Deixar mais humano
# * Verificar que a estrutura hierarquica ta fazendo mais ou menos sentido
# * Relatorio


from LinearDataStructure import *
from Array import *
from DoublyLinkedList import *
from DoublyNode import *
from Lista import *
from PilhaComLista import *
from Node import *
from Queue import *
from Stack import *
from PriorityQueue import *
from CircularLinkedList import *
from FiguraGeometrica import *
from matrix_final_refatorado import *

#
# ========== FUNÇÕES DE TESTE ==========
#



def test_array():
    print("=== TESTANDO CLASSE ARRAY ===")
    
    # 1. Teste de inicialização
    print("\n1. Teste de inicialização:")
    arr1 = Array()
    print(f"Array vazio: {arr1}")
    
    arr2 = Array([1, 2, 3])
    print(f"Array inicializado com [1, 2, 3]: {arr2}")
    
    arr3 = Array(range(5), initial_capacity=5)
    print(f"Array com range(5) e capacity=5: {arr3}")

    # 2. Teste de inserção
    print("\n2. Teste de inserção:")
    arr = Array([10, 20, 30])
    print(f"Array inicial: {arr}")
    
    arr.insert_start(5)
    print(f"Após insert_start(5): {arr}")
    
    arr.insert_end(40)
    print(f"Após insert_end(40): {arr}")
    
    arr.insert_at(2, 99)
    print(f"Após insert_at(2, 99): {arr}")
    
    # Teste de expansão automática
    print("\n3. Teste de expansão automática:")
    small_arr = Array(initial_capacity=3)
    print(f"Capacidade inicial: {small_arr._capacity}")
    
    for i in range(5):
        small_arr.insert_end(i)
        print(f"Após inserir {i}: tamanho={len(small_arr)}, capacidade={small_arr._capacity}")

    # 4. Teste de remoção
    print("\n4. Teste de remoção:")
    print(f"Array atual: {arr}")
    print(f"remove_start(): {arr.remove_start()}, Array: {arr}")
    print(f"remove_end(): {arr.remove_end()}, Array: {arr}")
    print(f"remove_at(1): {arr.remove_at(1)}, Array: {arr}")

    # 5. Teste de consulta (peek)
    print("\n5. Teste de consulta:")
    print(f"Array: {arr}")
    print(f"peek_start(): {arr.peek_start()}")
    print(f"peek_end(): {arr.peek_end()}")
    print(f"peek_at(1): {arr.peek_at(1)}")

    # 6. Teste de operador []
    print("\n6. Teste de operador []:")
    arr[0] = 100
    print(f"Após arr[0] = 100: {arr}")
    print(f"Valor de arr[1]: {arr[1]}")

    # 7. Teste de iteração
    print("\n7. Teste de iteração:")
    print("Elementos do array:", end=" ")
    for item in arr:
        print(item, end=" ")
    print()

    # 8. Teste de erros e casos especiais
    print("\n8. Teste de erros e casos especiais:")
    try:
        arr.insert_at(100, 0)
    except IndexError as e:
        print(f"Erro esperado ao insert_at(100, 0): {e}")
    
    try:
        arr.remove_at(100)
    except IndexError as e:
        print(f"Erro esperado ao remove_at(100): {e}")
    
    try:
        empty_arr = Array()
        empty_arr.remove_start()
    except IndexError as e:
        print(f"Erro esperado ao remover de array vazio: {e}")
    
    try:
        print(empty_arr.peek_start())
    except IndexError as e:
        print(f"Erro esperado ao peek_start() em array vazio: {e}")

    # 9. Teste de capacidade máxima
    print("\n9. Teste de capacidade máxima:")
    big_arr = Array(initial_capacity=2)
    print(f"Capacidade inicial: {big_arr._capacity}")
    for i in range(10):
        big_arr.insert_end(i)
    print(f"Após inserir 10 elementos: tamanho={len(big_arr)}, capacidade={big_arr._capacity}")
    print(f"Conteúdo: {big_arr}")

    print("\n=== TODOS OS TESTES CONCLUÍDOS ===")

def test_stack():
    print("=== TESTANDO CLASSE STACK ===")
    
    # 1. Teste de inicialização
    print("\n1. Teste de inicialização:")
    stack1 = Stack()
    print(f"Stack vazio: {stack1}, tamanho: {len(stack1)}")
    
    stack2 = Stack([1, 2, 3])
    print(f"Stack inicializado com [1, 2, 3]: {stack2}, tamanho: {len(stack2)}")
    
    # 2. Teste de push/pop
    print("\n2. Teste de push/pop:")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Após push(10), push(20), push(30): {stack}")
    
    print(f"pop(): {stack.pop()}")
    print(f"pop(): {stack.pop()}")
    print(f"Após dois pops: {stack}, tamanho: {len(stack)}")
    
    # 3. Teste de peek
    print("\n3. Teste de peek:")
    stack.push(40)
    stack.push(50)
    print(f"Stack atual: {stack}")
    print(f"peek_start() (topo): {stack.peek_start()}")
    print(f"peek_end() (base): {stack.peek_end()}")
    
    # 4. Teste de comportamento LIFO
    print("\n4. Teste de comportamento LIFO:")
    lifo_test = Stack()
    for i in range(1, 4):
        lifo_test.push(i)
        print(f"Push({i}): {lifo_test}")
    
    while not lifo_test.is_empty():
        print(f"Pop(): {lifo_test.pop()}, Stack: {lifo_test}")
    
    # 5. Teste de métodos adicionais
    print("\n5. Teste de métodos adicionais:")
    stack = Stack([10, 20, 30])
    print(f"Stack inicial: {stack}")
    
    stack.insert_start(5)  # Equivalente a push
    print(f"Após insert_start(5): {stack}")
    
    stack.insert_end(40)   # Insere na base
    print(f"Após insert_end(40): {stack}")
    
    print(f"remove_start(): {stack.remove_start()}")  # Equivalente a pop
    print(f"remove_end(): {stack.remove_end()}")     # Remove da base
    print(f"Stack após remoções: {stack}")
    
    # 6. Teste de iteração
    print("\n6. Teste de iteração:")
    stack = Stack([1, 2, 3])
    print("Elementos (topo para base):", end=" ")
    for item in stack:
        print(item, end=" ")
    print()
    
    # 7. Teste de erros e casos especiais
    print("\n7. Teste de erros e casos especiais:")
    empty_stack = Stack()
    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"Erro esperado ao pop() em stack vazia: {e}")
    
    try:
        empty_stack.peek_start()
    except IndexError as e:
        print(f"Erro esperado ao peek_start() em stack vazia: {e}")
    
    try:
        empty_stack.remove_end()
    except IndexError as e:
        print(f"Erro esperado ao remove_end() em stack vazia: {e}")
    
    # 8. Teste com diferentes tipos de dados
    print("\n8. Teste com diferentes tipos de dados:")
    complex_stack = Stack()
    complex_stack.push("string")
    complex_stack.push(3.14)
    complex_stack.push([1, 2, 3])
    print(f"Stack com tipos heterogêneos: {complex_stack}")
    print(f"pop(): {complex_stack.pop()}")
    
    # 9. Teste de grande volume
    print("\n9. Teste de grande volume:")
    big_stack = Stack()
    for i in range(100):
        big_stack.push(i)
    print(f"Stack com 100 elementos: tamanho={len(big_stack)}")
    
    print("\n=== TODOS OS TESTES CONCLUÍDOS ===")

def test_pilha_com_lista():
    print("=== TESTANDO PILHACOMLISTA E COMPARANDO COM STACK ===")
    
    def comparar_comportamento(pilha1, pilha2, operacao):
        """Função auxiliar para comparar o comportamento de duas implementações"""
        print(f"\nOperação: {operacao}")
        print(f"PilhaComLista: {pilha1}")
        print(f"StackOriginal: {pilha2}")
        assert len(pilha1) == len(pilha2), "Tamanhos diferentes!"
        if not pilha1.is_empty():
            assert pilha1.top() == pilha2.peek_start(), "Topo diferente!"
    
    # 1. Teste de inicialização
    print("\n1. Teste de inicialização:")
    pl = PilhaComLista([1, 2, 3])
    st = Stack([1, 2, 3])
    comparar_comportamento(pl, st, "Inicialização com [1, 2, 3]")
    
    # 2. Teste de push/pop
    print("\n2. Teste de push/pop:")
    pl.push(10)
    st.push(10)
    comparar_comportamento(pl, st, "Após push(10)")
    
    pl.push(20)
    st.push(20)
    comparar_comportamento(pl, st, "Após push(20)")
    
    print(f"pl.pop(): {pl.pop()}")
    print(f"st.pop(): {st.pop()}")
    comparar_comportamento(pl, st, "Após pop()")
    
    # 3. Teste de top/peek
    print("\n3. Teste de top/peek:")
    print(f"pl.top(): {pl.top()}")
    print(f"st.peek_start(): {st.peek_start()}")
    comparar_comportamento(pl, st, "Comparação após top()/peek_start()")
    
    # 4. Teste de comportamento LIFO
    print("\n4. Teste de comportamento LIFO:")
    test_items = ['a', 'b', 'c']
    pl_lifo = PilhaComLista(test_items)
    st_lifo = Stack(test_items)
    
    for i in range(3):
        comparar_comportamento(pl_lifo, st_lifo, f"Estado {i}")
        print(f"pl.pop(): {pl_lifo.pop()}")
        print(f"st.pop(): {st_lifo.pop()}")
    
    # 5. Teste de pilha vazia
    print("\n5. Teste de pilha vazia:")
    empty_pl = PilhaComLista()
    empty_st = Stack()
    comparar_comportamento(empty_pl, empty_st, "Pilhas vazias")
    
    try:
        empty_pl.pop()
    except IndexError as e:
        print(f"PilhaComLista levantou IndexError ao pop() vazio: {e}")
    
    try:
        empty_st.pop()
    except IndexError as e:
        print(f"Stack levantou IndexError ao pop() vazio: {e}")
    
    # 6. Teste com diferentes tipos de dados
    print("\n6. Teste com diferentes tipos de dados:")
    complex_pl = PilhaComLista()
    complex_st = Stack()
    
    items = [1, "string", 3.14, [1, 2, 3]]
    for item in items:
        complex_pl.push(item)
        complex_st.push(item)
    
    comparar_comportamento(complex_pl, complex_st, "Pilhas com tipos complexos")
    
    # 7. Teste de grande volume
    print("\n7. Teste de grande volume:")
    big_pl = PilhaComLista(range(1000))
    big_st = Stack(range(1000))
    comparar_comportamento(big_pl, big_st, "Pilhas com 1000 elementos")
    
    print("\n=== TODOS OS TESTES CONCLUÍDOS COM SUCESSO ===")

def test_priority_queue():
    print("\n=== TESTANDO FILA DE PRIORIDADES ===")
    
    # Classe auxiliar para itens com prioridade
    class Task:
        def __init__(self, name, priority):
            self.name = name
            self.priority = priority  # Quanto menor o número, maior a prioridade
        
        def __repr__(self):
            return f"{self.name} (prio:{self.priority})"
    
    # Teste 1: Criação da fila de prioridades vazia
    print("\nTeste 1: Criação de fila vazia")
    pq = DoublyLinkedList()
    print(f"Fila vazia: {list(pq)} (esperado: [])")
    
    # Teste 2: Inserção ordenada de tarefas
    print("\nTeste 2: Inserção ordenada")
    tasks = [
        Task("Lavar louça", 3),
        Task("Estudar para prova", 1),
        Task("Fazer compras", 2),
        Task("Ler livro", 4)
    ]
    
    for task in tasks:
        pq.insert_ordered(task, key=lambda x: x.priority)
    
    print("\nTarefas ordenadas por prioridade:")
    for i, task in enumerate(pq):
        print(f"{i+1}º: {task}")
    
    # Resultado esperado:
    # 1º: Estudar para prova (prio:1)
    # 2º: Fazer compras (prio:2)
    # 3º: Lavar louça (prio:3)
    # 4º: Ler livro (prio:4)
    
    # Teste 3: Processamento da fila (removendo sempre a maior prioridade)
    print("\nTeste 3: Processamento da fila (FIFO por prioridade)")
    print("\nProcessando tarefas...")
    while len(pq) > 0:
        task = pq.pop()
        print(f"Processando: {task}")
    
    # Resultado esperado:
    # Processando: Estudar para prova (prio:1)
    # Processando: Fazer compras (prio:2)
    # Processando: Lavar louça (prio:3)
    # Processando: Ler livro (prio:4)
    
    # Teste 4: Inserção com prioridades iguais (deve manter ordem de inserção)
    print("\nTeste 4: Prioridades iguais (ordem de inserção)")
    pq = DoublyLinkedList()
    pq.insert_ordered(Task("Tarefa A", 2), key=lambda x: x.priority)
    pq.insert_ordered(Task("Tarefa B", 1), key=lambda x: x.priority)
    pq.insert_ordered(Task("Tarefa C", 2), key=lambda x: x.priority)
    
    print("\nTarefas com prioridades iguais:")
    for task in pq:
        print(task)
    
    # Resultado esperado:
    # Tarefa B (prio:1)
    # Tarefa C (prio:2)
    # Tarefa A (prio:2)

def test_doubly_linked_list():
    print("\n=== TESTANDO DOUBLYLINKEDLIST ===")
    
    # Teste 1: Criação a partir de lista de inicialização
    print("\nTeste 1: Criação a partir de lista")
    dll = DoublyLinkedList([3, 1, 4, 2])
    print(f"Lista inicial: {list(dll)} (esperado: [3, 1, 4, 2])")
    
    # Teste 2: Inserção no início e no fim
    print("\nTeste 2: Inserção push/push_back")
    dll.push(0)          # Alias para insert_start
    dll.insert_end(5)     # Alias para insert_end
    print(f"Após inserções: {list(dll)} (esperado: [0, 3, 1, 4, 2, 5])")
    
    # Teste 3: Remoção do início e do fim
    print("\nTeste 3: Remoção pop/pop_back")
    first = dll.pop()    # Alias para remove_start
    last = dll.remove_end() # Alias para remove_end
    print(f"Removido primeiro: {first} (esperado: 0)")
    print(f"Removido último: {last} (esperado: 5)")
    print(f"Lista após remoções: {list(dll)} (esperado: [3, 1, 4, 2])")
    
    # Teste 4: Consulta sem remoção
    print("\nTeste 4: Consulta get_item")
    item = dll.peek_at(2)
    print(f"Item na posição 2: {item} (esperado: 4)")
    
    # Teste 5: Troca de elementos (swap)
    print("\nTeste 5: Troca de elementos adjacentes")
    print(f"Antes do swap: {list(dll)}")
    dll.swap(1)  # Troca posições 1 e 2 (valores 1 e 4)
    print(f"Após swap(1): {list(dll)} (esperado: [3, 4, 1, 2])")
    
    # Teste 6: Ordenação com bubble_sort
    print("\nTeste 6: Ordenação bubble_sort")
    dll.bubble_sort()
    print(f"Lista ordenada: {list(dll)} (esperado: [1, 2, 3, 4])")
    
    # Teste 7: Iteração reversa
    print("\nTeste 7: Iteração reversa")
    print(f"Lista em reverso: {list(reversed(dll))} (esperado: [4, 3, 2, 1])")
    
    # Teste 8: Inserção em posição específica
    print("\nTeste 8: Inserção em posição específica")
    dll.insert_at(2, 2.5)
    print(f"Após inserção: {list(dll)} (esperado: [1, 2, 2.5, 3, 4])")
    
    # Teste 9: Remoção em posição específica
    print("\nTeste 9: Remoção em posição específica")
    removed = dll.remove_at(3)
    print(f"Removido: {removed} (esperado: 3)")
    print(f"Lista final: {list(dll)} (esperado: [1, 2, 2.5, 4])")

def integrated_test():
    print("\n=== TESTE INTEGRADO ===")
    
    # Teste com diferentes tipos de dados
    print("\nTestando com diferentes tipos:")
    mixed_list = DoublyLinkedList()
    mixed_list.insert_end("String")
    mixed_list.insert_end(42)
    mixed_list.insert_end(3.14)
    mixed_list.insert_end(True)
    
    print(f"Lista com tipos mistos: {list(mixed_list)}")
    print(f"Tamanho da lista: {len(mixed_list)} (esperado: 4)")
    
    # Teste de stress com muitos elementos
    print("\nTeste de stress com 1000 elementos:")
    big_list = DoublyLinkedList(range(1000))
    print(f"Tamanho: {len(big_list)} (esperado: 1000)")
    print(f"Primeiro elemento: {big_list.peek_at(0)} (esperado: 0)")
    print(f"Último elemento: {big_list.peek_at(999)} (esperado: 999)")
    
    # Ordenação de lista grande
    print("\nOrdenando lista grande...")
    reversed_big_list = DoublyLinkedList(range(1000, 0, -1))
    reversed_big_list.bubble_sort()
    print(f"Primeiro elemento após ordenação: {reversed_big_list.peek_at(0)} (esperado: 1)")
    print(f"Último elemento após ordenação: {reversed_big_list.peek_at(999)} (esperado: 1000)")

def testar_fila_bandejao():
    """Função para testar todas as funcionalidades da FilaBandejao"""
    print("=== TESTE COMPLETO FILA BANDEJÃO ===")
    print("=== Configuração inicial ===")
    fila = FilaBandejao(tempo_medio_atendimento=2)
    print(f"Tempo médio de atendimento: {fila.tempo_medio} minutos")
    
    # Criando pratos
    pratos = {
        "feijoada": Prato("Feijoada Completa", 5),
        "lasanha": Prato("Lasanha à Bolonhesa", 4),
        "vegetariano": Prato("Prato Vegetariano", 3)
    }
    
    # Criando usuários
    usuarios = [
        Usuario(1, "João Silva"),
        Usuario(2, "Maria Oliveira"),
        Usuario(3, "Carlos Souza"),
        Usuario(4, "Ana Santos")
    ]
    
    print("\n=== Teste 1: Adicionando usuários na fila ===")
    fila.enqueue(usuarios[0], pratos["feijoada"])
    fila.enqueue(usuarios[1], pratos["lasanha"])
    print(f"Fila após adicionar 2 usuários: {list(fila)}")
    print(f"Tempo espera atual: {fila.tempo_espera_atual()} min (esperado: 4 min)")
    print(f"Próximo: {fila.peek_start().nome} (esperado: João Silva)")
    print(f"Tempo estimado João: {usuarios[0].tempo_estimado} min (esperado: 2 min)")
    print(f"Tempo estimado Maria: {usuarios[1].tempo_estimado} min (esperado: 4 min)")
    
    print("\n=== Teste 2: Adicionando mais um usuário ===")
    fila.enqueue(usuarios[2], pratos["vegetariano"])
    print(f"Tempo espera atual: {fila.tempo_espera_atual()} min (esperado: 6 min)")
    print(f"Tempo estimado Carlos: {usuarios[2].tempo_estimado} min (esperado: 6 min)")
    
    print("\n=== Teste 3: Atendimento (dequeue) ===")
    atendido = fila.dequeue()
    print(f"Atendido: {atendido.nome} (esperado: João Silva)")
    print(f"Fila após atendimento: {list(fila)}")
    print(f"Novo tempo estimado Maria: {usuarios[1].tempo_estimado} min (esperado: 2 min)")
    print(f"Novo tempo estimado Carlos: {usuarios[2].tempo_estimado} min (esperado: 4 min)")
    
    print("\n=== Teste 4: Desistência ===")
    print(f"Desistência de Carlos (id 3): {fila.desistencia(3)} (esperado: True)")
    print(f"Fila após desistência: {list(fila)} (esperado: [Maria Oliveira])")
    print(f"Novo tempo estimado Maria: {usuarios[1].tempo_estimado} min (esperado: 2 min)")
    
    print("\n=== Teste 5: Atraso no atendimento ===")
    fila.registrar_atraso(3)
    print(f"Tempo espera atual: {fila.tempo_espera_atual()} min (esperado: 5 min)")
    print(f"Novo tempo estimado Maria: {usuarios[1].tempo_estimado} min (esperado: 5 min)")
    
    print("\n=== Teste 6: Adicionando mais usuários com atraso ===")
    fila.enqueue(usuarios[3], pratos["feijoada"])
    print(f"Fila: {list(fila)} (esperado: [Maria Oliveira, Ana Santos])")
    print(f"Tempo estimado Ana: {usuarios[3].tempo_estimado} min (esperado: 10 min)")
    
    print("\n=== Teste 7: Adiantamento ===")
    fila.registrar_adiantamento(2)
    print(f"Tempo espera atual: {fila.tempo_espera_atual()} min (esperado: 6 min)")
    print(f"Tempo estimado Maria: {usuarios[1].tempo_estimado} min (esperado: 3 min)")
    print(f"Tempo estimado Ana: {usuarios[3].tempo_estimado} min (esperado: 6 min)")
    
    print("\n=== Teste 8: Busca de usuário ===")
    usuario = fila.get_usuario(2)
    print(f"Usuário id 2: {usuario.nome if usuario else 'Não encontrado'} (esperado: Maria Oliveira)")
    usuario = fila.get_usuario(99)
    print(f"Usuário id 99: {usuario.nome if usuario else 'Não encontrado'} (esperado: Não encontrado)")
    
    print("\n=== Teste 9: Tentativas de erro ===")
    try:
        fila.dequeue()
        fila.dequeue()
        fila.dequeue()
    except IndexError as e:
        print(f"Erro ao atender fila vazia: {e} (esperado: Fila vazia)")

def testar_calculadora_matricial():
    print("\n=== TESTE DA CALCULADORA MATRICIAL ===")
    
    # Criando uma instância da calculadora
    calculadora = CalculadoraMatricial()
    
    # Teste 1: Adicionar matriz regular
    print("\nTeste 1: Adicionar matriz regular 2x3")
    matriz1 = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ]
    idx1 = calculadora.adicionar_matriz_com_nome(matriz1, "Matriz A")
    print(f"Matriz adicionada no índice {idx1}:")
    print(calculadora.matrizes[idx1])
    print("Resultado esperado:")
    print("1.00 2.00 3.00\n4.00 5.00 6.00")
    
    # Teste 2: Adicionar matriz quadrada
    print("\nTeste 2: Adicionar matriz quadrada 2x2")
    matriz2 = [
        [1.0, 2.0],
        [3.0, 4.0]
    ]
    idx2 = calculadora.adicionar_matriz_com_nome(matriz2, "Matriz B")
    print(f"Matriz adicionada no índice {idx2}:")
    print(calculadora.matrizes[idx2])
    print("Resultado esperado:")
    print("1.00 2.00\n3.00 4.00")
    
    # Teste 3: Soma de matrizes
    print("\nTeste 3: Soma de matrizes (A + B)")
    try:
        resultado_soma = calculadora.operacao(idx1, '+', idx2)
        print("Erro: A soma deveria falhar para matrizes de dimensões diferentes")
    except ValueError as e:
        print(f"Erro esperado: {str(e)}")
    
    # Teste 4: Multiplicação por escalar
    print("\nTeste 4: Multiplicação por escalar (B * 2)")
    resultado_escalar = calculadora.operacao(idx2, '*', 2)
    print("Resultado:")
    print(resultado_escalar)
    print("Resultado esperado:")
    print("2.00 4.00\n6.00 8.00")
    
    # Teste 5: Multiplicação de matrizes
    print("\nTeste 5: Multiplicação de matrizes (B * B)")
    resultado_mult = calculadora.operacao(idx2, '*', idx2)
    print("Resultado:")
    print(resultado_mult)
    print("Resultado esperado:")
    print("7.00 10.00\n15.00 22.00")
    
    # Teste 6: Transposta
    print("\nTeste 6: Transposta da matriz A")
    resultado_transposta = calculadora.operacao(idx1, 'T')
    print("Resultado:")
    print(resultado_transposta)
    print("Resultado esperado:")
    print("1.00 4.00\n2.00 5.00\n3.00 6.00")
    
    # Teste 7: Traço
    print("\nTeste 7: Traço da matriz B")
    resultado_traco = calculadora.operacao(idx2, 'tr')
    print("Resultado:")
    print(resultado_traco)
    print("Resultado esperado:")
    print("5.0")
    
    # Teste 8: Determinante
    print("\nTeste 8: Determinante da matriz B")
    resultado_det = calculadora.operacao(idx2, 'det')
    print("Resultado:")
    print(resultado_det)
    print("Resultado esperado:")
    print("-2.0")
    
    # Teste 9: Matriz identidade
    print("\nTeste 9: Adicionar matriz identidade 3x3")
    idx_ident = calculadora.adicionar_matriz_identidade(3, "Identidade 3x3")
    print(f"Matriz adicionada no índice {idx_ident}:")
    print(calculadora.matrizes[idx_ident])
    print("Resultado esperado:")
    print("1.00 0.00 0.00\n0.00 1.00 0.00\n0.00 0.00 1.00")
    
    # Teste 10: Listar todas as matrizes
    print("\nTeste 10: Listar todas as matrizes")
    print("Resultado:")
    calculadora.listar_matrizes()
    print("Resultado esperado:")
    print("Deve listar todas as matrizes adicionadas nos testes anteriores")
    
    print("\n=== FIM DOS TESTES ===")

def test_figura_geometrica():
    print("=== TESTE DA CLASSE FIGURA GEOMÉTRICA ===")
    
    # 1. Criação de uma figura com 4 vértices (quadrado)
    print("\n1. Criando um quadrado válido:")
    quadrado = FiguraGeometrica(max_vertices=4)
    vertices_quadrado = [(0, 0), (1, 0), (1, 1), (0, 1)]
    for vertice in vertices_quadrado:
        quadrado.adicionar_vertice(vertice)
    print(f"   Resultado: {quadrado}")
    print(f"   Esperado: FiguraGeometrica([(0, 0), (1, 0), (1, 1), (0, 1)])")

    # 2. Tentativa de adicionar vértice a uma figura cheia
    print("\n2. Tentando adicionar 5º vértice ao quadrado (deve falhar):")
    try:
        quadrado.adicionar_vertice((0.5, 0.5))
    except OverflowError as e:
        print(f"   Resultado: {e}")
        print(f"   Esperado: Número máximo de vértices atingido")

    # 3. Criação de uma figura com 3 vértices (triângulo)
    print("\n3. Criando um triângulo válido:")
    triangulo = FiguraGeometrica(max_vertices=3)
    vertices_triangulo = [(0, 0), (2, 0), (1, 2)]
    for vertice in vertices_triangulo:
        triangulo.adicionar_vertice(vertice)
    print(f"   Resultado: {triangulo}")
    print(f"   Esperado: FiguraGeometrica([(0, 0), (2, 0), (1, 2)])")

    # 4. Tentativa de criar figura com linhas cruzadas (estrela inválida)
    print("\n4. Tentando criar figura com linhas cruzadas (deve falhar):")
    estrela_invalida = FiguraGeometrica(max_vertices=5)
    vertices_invalidos = [(0, 0), (2, 2), (2, 0), (0, 2), (1, 1)]  # Cruzamento no centro
    try:
        for vertice in vertices_invalidos:
            estrela_invalida.adicionar_vertice(vertice)
    except ValueError as e:
        print(f"   Erro ao adicionar vértice (1, 1): {e}")
        print(f"   Esperado: A adição deste vértice causaria linhas cruzadas")

    # 5. Teste com polígono convexo (hexágono)
    print("\n5. Criando hexágono convexo válido:")
    hexagono = FiguraGeometrica(max_vertices=6)
    vertices_hexagono = [(0, 0), (1, 0), (1.5, 0.87), (1, 1.73), (0, 1.73), (-0.5, 0.87)]
    for vertice in vertices_hexagono:
        hexagono.adicionar_vertice(vertice)
    print(f"   Resultado: {hexagono}")
    print(f"   Esperado: FiguraGeometrica({vertices_hexagono})")

    # 6. Teste com inicialização direta via iterável
    print("\n6. Inicialização direta com iterável:")
    pentagono = FiguraGeometrica(
        max_vertices=5,
        vertices=[(0, 0), (1, 0), (1.3, 0.8), (0.5, 1.3), (-0.3, 0.8)]
    )
    print(f"   Resultado: {pentagono}")
    print("   Esperado: FiguraGeometrica([(0, 0), (1, 0), (1.3, 0.8), (0.5, 1.3), (-0.3, 0.8)])")

def test_circular_linked_list():
    print("=== TESTANDO CIRCULARLINKEDLIST ===")
    
    # 1. Criação da lista com tamanho fixo e inicialização
    lista = CircularLinkedList(max_size=5, iterable=[3, 1, 4])
    print(f"Lista inicial: {list(lista)}")  # Usando list() para evitar loops
    print(f"   Esperado: CircularLinkedList([3, 1, 4])")
    print(f"   Tamanho: {len(lista)} | Esperado: 3")
    print(f"   Está cheia? {lista.is_full()} | Esperado: False")
    
    # 2. Inserção no início e no final
    lista.insert_start(0)
    lista.insert_end(5)
    print(f"\n2. Após inserir 0 no início e 5 no final: {list(lista)}")
    print(f"   Esperado: CircularLinkedList([0, 3, 1, 4, 5])")
    print(f"   Tamanho: {len(lista)} | Esperado: 5")
    print(f"   Está cheia? {lista.is_full()} | Esperado: True")
    
    # 3. Tentativa de inserção em lista cheia (VAI falhar)
    try:
        lista.insert_end(99)
    except OverflowError as e:
        print(f"\n3. Tentativa de inserir em lista cheia: {e}")
        print(f"   Esperado: OverflowError('Lista circular está cheia')")
    
    # 4. Remoção do início e do final
    primeiro = lista.remove_start()
    ultimo = lista.remove_end()
    print(f"\n4. Removeu início ({primeiro}) e final ({ultimo}): {list(lista)}")
    print(f"   Esperado: CircularLinkedList([3, 1, 4])")
    print(f"   Tamanho: {len(lista)} | Esperado: 3")
    
    # 5. Consulta sem remoção (peek)
    print(f"\n5. Consulta:")
    print(f"   Primeiro elemento: {lista.peek_start()} | Esperado: 3")
    print(f"   Elemento na posição 1: {lista.peek_at(1)} | Esperado: 1")
    print(f"   Último elemento: {lista.peek_end()} | Esperado: 4")
    
    # 6. Troca de posições consecutivas (swap)
    lista.swap(0, 1)  # Troca 3 e 1
    print(f"\n6. Após swap(0, 1): {list(lista)}")
    print(f"   Esperado: CircularLinkedList([1, 3, 4])")
    
    # 7. Ordenação (bubble-sort)
    lista.sort()
    print(f"\n7. Após sort(): {list(lista)}")
    print(f"   Esperado: CircularLinkedList([1, 3, 4])")
    
    # 8. Iteração (__iter__)
    print(f"\n8. Iteração:")
    elementos = [str(item) for item in lista]
    print(f"   Elementos iterados: {', '.join(elementos)} | Esperado: 1, 3, 4")


# função main pra testar tuod
if __name__ == "__main__":
    # test_array()
    # test_stack()
    # test_pilha_com_lista()
    # test_doubly_linked_list()
    # test_priority_queue()
    # integrated_test()
    # testar_fila_bandejao()
    # test_circular_linked_list()
    # test_figura_geometrica()
    # testar_calculadora_matricial()
    pass