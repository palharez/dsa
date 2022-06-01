"""
# Pilhas - Stack

**Pilha** ou _stack_ é um tipo especial de lista linear em que todas as operações de inserção e remoção são realizadas pela mesma extremidade chamada de **topo**, em oposição a outra extremidade, chamada de base.

Os elementos são removidos na ordem do programa inversa daquela em que foram inseridos de modo que o último elemento que entra é sempre o primeiro a ser executado, por isto este tipo de estrutura é chamada **LIFO** (Last In - First Out).

A implementação de pilhas pode ser realizada através de vetor ou através de listas encadeadas.

**Exemplos de uso de pilha em um sistema:**

- Funções recursivas em compiladores;
- Mecanismo de desfazer/refazer dos editores de texto;
- Navegação entre páginas Web.

**Operações com Pilha:**

- Criação da pilha (informar a capacidade no caso de implementação sequencial - vetor);
- Empilhar (push);
- Desempilhar (pop);
- Mostrar o topo (peek);
- Verificar se a pilha está vazia (is_empty);
- Verificar o tamanho da pilha (size);

"""

class Stack: #Stack

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1


    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1
    
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        if self.len_stack == 0:
            return True
        return False
    
    def length(self):
        return self.len_stack
