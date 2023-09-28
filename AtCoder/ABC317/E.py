from collections import deque

H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2
N = H2 * W2

Empty = 0
Wall = 1
Sight = 2

Persons = []

M = [Wall] * N

for h in range(1, H + 1):
    A = input()
    for i, c in enumerate(A, h * W2 + 1):
        x = Wall
        if c == "S":
            x = Empty
            start = i
        if c == "G":
            x = Empty
            goal = i
        if c == ".":
            x = Empty
        if c == "<":
            Persons.append((i, -1))
        if c == ">":
            Persons.append((i, +1))
        if c == "^":
            Persons.append((i, -W2))
        if c == "v":
            Persons.append((i, +W2))

        M[i] = x

for i, dir in Persons:
    j = i + dir
    while M[j] != Wall:
        M[j] = Sight
        j += dir

dist = [-1] * N
queue = deque([start])

while queue:
    q = queue.popleft()
    d = q // N
    i = q % N
    if dist[i] != -1 or M[i] != Empty:
        continue
    dist[i] = d

    queue.append(q + N - 1)
    queue.append(q + N + 1)
    queue.append(q + N - W2)
    queue.append(q + N + W2)


print(dist[goal])
