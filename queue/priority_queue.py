'''
    Implementação da priority queue com lista ordenada
'''


class Person:
    '''
        nome -> nome da pessoa
        prior -> prioridade da pessoa
    '''

    def __init__(self, name, prior):
        self.name = name
        self.prior = prior

    def getName(self):
        return self.name

    def getPrior(self):
        return self.prior


class PriorityQueue:
    def __init__(self):
        self.pq = []  # priority queue
        self.len = 0  # length of priority queue

    # insere decrescentemente pela prioridade
    def push(self, person):
        if self.empty():
            self.pq.append(person)
        else:
            flagPush = False
            # procura se onde inserir para manter a fila ordenada
            for i in range(self.len):
                if self.pq[i].getPrior() < person.getPrior():
                    self.pq.insert(i, person)
                    flagPush = True
                    break

            if not flagPush:
                # se entrou aqui é porque tem que inserir ao final
                self.pq.insert(self.len, person)

        self.len += 1

    def pop(self):
        if not self.empty():
            self.pq.pop(0)
            self.len -= 1

    def empty(self):
        if self.len == 0:
            return True
        return False

    def show(self):
        for p in self.pq:
            print('Nome: %s' % p.getName())
            print('Prioridade: %d\n' % p.getPrior())


# criando os objetos Person
p1 = Person('Eduardo', 21)
p2 = Person('Joana', 18)
p3 = Person('Leonardo', 8)
p4 = Person('Adriana', 42)

# criando a fila de prioridade e inserindo elementos
pq = PriorityQueue()
pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)

print('Exibindo após a inserções: \n')
pq.show()  # Adriana Eduardo Joana Leonardo

# removendo elementos
pq.pop()
pq.pop()

print('Exibindo após as remoçãos:\n')
pq.show()  # Joana Leonardo

# inserindo um novo elemento
pq.push(Person('Maria', 80))
print('Exibindo após a inserção:\n')
pq.show()  # Maria Joana Leonardo
