matriz = [
    ['joão', 8, 7, 6],
    ['pedro', 4.5, 9, 10],
    ['marcos', 6, 6, 8]
]

for lin in matriz:
    for col in lin:
        print(str(col) + '\t', end = ' ')
    print('')