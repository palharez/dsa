class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None


class ListaLigada:

    def __init__(self):
        self._inicio = None
        self._quantidade = 0
    
    @property
    def inicio(self):
        return self._inicio


    @property
    def quantidade(self):
        return self._quantidade

    def inserir_no_inicio(self, conteudo):
        celula = Celula(conteudo)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1

    def imprimir(self):
        atual = self.inicio
        for _ in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

    def _celula(self, posicao):
        self._validiar_posicao(posicao)
        atual = self.inicio

        for _ in range(0, posicao):
            atual = atual.proximo

        return atual

    def _validiar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError(f"Posição inválida {posicao}")

    def inserir(self, posicao, conteudo):
        if posicao == 0:
            self.inserir_no_inicio(conteudo)
            return
        
        celula = Celula(conteudo)
        esquerda = self._celula(posicao-1) 
        celula.proximo = esquerda.proximo
        esquerda.proximo = celula
        self._quantidade += 1
    
    def remover_do_inicio(self):
        removido = self.inicio
        self._inicio = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def remover(self, posicao):
        if posicao == 0:
            return self.remover_do_inicio()

        esquerda = self._celula(posicao - 1)
        removido = esquerda.proximo
        esquerda.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def item(self, posicao):
        celula = self._celula(posicao)
        return celula.conteudo