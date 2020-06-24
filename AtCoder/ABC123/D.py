X, Y, Z, K = [int(c) for c in input().split()]
A, B, C = [sorted(map(int, input().split()), reverse=True) for _ in range(3)]

AB = []
for a in A:
    for b in B:
        AB.append(a+b)

ABC = []
for ab in sorted(AB, reverse=True)[:K]:
    for c in C:
        ABC.append(ab+c)

for abc in sorted(ABC, reverse=True)[:K]:
    print(abc)
