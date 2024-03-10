from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

D = defaultdict(int)
for a in A:
    D[a] += 1

C = list(D.values())
C.sort(reverse=True)
C.append(0)

n = 0
s = 0
KX = [None] * (N + 1)
for X in range(N, 0, -1):
    while C[n] > X:
        s += C[n]
        n += 1

    K = (N - s + n * X) // X

    if KX[K] is None:
        KX[K] = X

v = 0
for i in range(N, 0, -1):
    if KX[i] is None:
        KX[i] = v
    else:
        v = KX[i]

for ans in KX[1:]:
    print(ans)
