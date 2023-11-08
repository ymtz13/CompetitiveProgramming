from random import shuffle, seed

seed(0)

print(200, 10)

A = list(range(1, 201))
shuffle(A)

for m in range(10):
    print(*A[m * 20 : m * 20 + 20])
