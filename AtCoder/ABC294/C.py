N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A[:] + B[:]
C.sort()

D = {}
for i, c in enumerate(C, 1):
    D[c] = i

ansA = []
for a in A:
    ansA.append(D[a])

ansB = []
for b in B:
    ansB.append(D[b])

print(*ansA)
print(*ansB)
