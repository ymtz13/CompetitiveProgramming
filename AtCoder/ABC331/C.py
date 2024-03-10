N = int(input())
A = list(map(int, input().split()))

X = sorted(A, reverse=True)
s = 0
p = 1 << 60

D = {}

for a in X:
    if a != p:
        p = a
        D[a] = s
    s += a


print(*[D[a] for a in A])
