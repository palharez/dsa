"""
    Cada elemento da posição i será comparado com o elmento da posição i + 1,
    e quando a ordernação procurada é encontrada, uma troca de posições entre
    os elmentos é feita.

    Tempo de excução do algoritmo:
     O(n²) 

    Não existe melhor e pior situação ele sempre se comportará da mesma maneira.
"""

def bubble_sort(V):
    aux = 0
    # Ordenando de forma crescente
    # laço com a quantidade de elementos do vetor
    for n in range(len(V)):
        # laço que percore da primeira á penúltima posição do vetor
        for i in range(len(V) - 1):
            if V[i] > V[i + 1]:
                aux = V[i]
                V[i] = V[i + 1]
                V[i + 1] = aux

    return V

if __name__ == "__main__":
    print(bubble_sort([4, 2, 3, 1]))  # 1, 2, 3, 4