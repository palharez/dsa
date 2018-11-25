from collections import deque

d = deque()
d.append(1) # adiciona do lado direito
d.appendleft(2) # adiciona do lado esquerda 
d.append(3)
d.appendleft(4)

for i in d:
    print(i, end= ' ')
    # 4, 2, 1, 3

print()
# d.pop()
# d.popleft()

d.remove(2)

for i in d:
    print(i, end= ' ')