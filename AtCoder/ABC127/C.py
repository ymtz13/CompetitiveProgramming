N, M = [int(c) for c in input().split()]

L, R = [], []
for i in range(M):
    l, r = [int(c) for c in input().split()]
    L.append(l)
    R.append(r)

print(max(min(R)-max(L)+1, 0))
