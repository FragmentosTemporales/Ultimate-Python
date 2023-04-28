from collections import deque

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
print(fila)
fila.pop()
print(fila)
fila.popleft()
print(fila)
fila.popleft()
fila.popleft()
fila.popleft()
if not fila:
    print("fila vacia")
    