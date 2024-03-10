N = int(input())
A = list(map(int, input().split()))

L = []
m = 0
for a in A:
    m = min(a, m + 1)
    L.append(m)

R = []
m = 0
for a in reversed(A):
    m = min(a, m + 1)
    R.append(m)

R.reverse()

X = [min(l, r) for l, r in zip(L, R)]

print(max(X))
