"""
 Função de complexido de tempo O(n - 1), é o numero de comparações entre os elementos de A
"""

def calculamenor(A, n):
    menor = A[0]
    for i in range(1, n):
        if A[i] < menor:
            menor = A[i]
    return menor
    
if __name__ == "__main__":
    print(calculamenor([30, 31, 3, 50, 59, 6], 5) == 3)  # True