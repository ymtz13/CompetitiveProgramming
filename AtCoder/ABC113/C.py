N, M = list(map(int, input().split()))

C = []
for i in range(M):
    P, Y = list(map(int, input().split()))
    C.append((i, P, Y))
C = sorted(C, key=lambda x:x[1])

K, L = [], []
p = C[0][1]
for c in C:
    if c[1]!=p:
        p = c[1]
        L += [ (k[0], k[1], i+1) for i, k in enumerate(sorted(K, key=lambda x:x[2]))]
        K = []

    K.append(c)

L += [ (k[0], k[1], i+1) for i, k in enumerate(sorted(K, key=lambda x:x[2]))]

for l in sorted(L, key=lambda x:x[0]):
    print('{:06d}{:06d}'.format(l[1],l[2]))
