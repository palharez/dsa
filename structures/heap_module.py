'''
    Implementação da priority queue com uma Heap Binária
'''
import heapq


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    # Faz com que o objeto seja impresso de forma legível
    def __repr__(self):
        return self.nome


class FilaDePrioridade:
    def __init__(self):
        self._fila = []
        self._indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self._fila, (-prioridade, self._indice, item))
        self._indice += 1

    def remover(self):
        return heapq.heappop(self._fila)[-1]


fila = FilaDePrioridade()

fila.inserir(Pessoa('Eduardo'), 21)
fila.inserir(Pessoa('Joana'), 18)
fila.inserir(Pessoa('Adriana'), 30)
fila.inserir(Pessoa('Leonardo'), 26)

print(fila.remover())  # Adriana
