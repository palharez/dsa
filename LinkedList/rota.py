from lista_ligada import ListaLigada, Celula

class Loja:
    
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f"{self.nome}, {self.endereco}"


def main():
    loja1 = Loja('Mercadinho', 'Rua das Laranjeira, 12')
    loja2 = Loja('Hortifruti', 'Rua do Pomar, 300')
    loja3 = Loja('Padaria', 'Rua das Flores, 600')
    loja4 = Loja('Supermercado', 'Alameda Santos, 400')
    loja5 = Loja('Mini Mercado', 'Rua da Fazenda, 100')
    loja6 = Loja('Quitanda', 'Avenida Rio Branco, 34')


    lista = ListaLigada()
    print(lista.quantidade)

    lista.inserir_no_inicio(loja1)
    print(lista.quantidade)
    lista.imprimir()

    lista.inserir_no_inicio(loja2)
    print(lista.quantidade)
    lista.imprimir()

    lista.inserir_no_inicio(loja3)
    print(lista.quantidade)
    lista.imprimir()

    lista.inserir(1, loja4)
    print(lista.quantidade)
    lista.imprimir()

    lista.inserir(0, loja5)
    print(lista.quantidade)
    lista.imprimir()

    lista.inserir(lista.quantidade, loja6)
    print(lista.quantidade)
    lista.imprimir()

    removido = lista.remover_do_inicio()
    print(lista.quantidade)
    lista.imprimir()
    print(f"Removido: {removido}")

    removido = lista.remover_do_inicio()
    print(lista.quantidade)
    lista.imprimir()
    print(f"Removido: {removido}")

    removido = lista.remover(1)
    print(lista.quantidade)
    lista.imprimir()
    print(f"Removido da posicao 1: {removido}")

    removido = lista.remover(lista.quantidade - 1)
    print(lista.quantidade)
    lista.imprimir()
    print(f"Removido: {removido}")

    print(f"Item 0 da lista {lista.item(0)}")

if __name__ == '__main__':
    main()