"""
    recorrência: é uma equação ou desigualdade que descreve uma função em termos de seu
     valor em entradas menores
    
    Tempo de execução:
     T(n) = (n - 1) + 1
"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    print(fatorial(5) == 120)  # True