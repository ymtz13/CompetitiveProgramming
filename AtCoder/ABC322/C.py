N, M = map(int, input().split())
A = list(map(int, input().split()))

X = [1 << 60] * (N + 1)
for a in A:
    X[a] = 0

v = 0
for i in range(N, 0, -1):
    if X[i] == 0:
        v = 0
    else:
        v += 1
        X[i] = v

for x in X[1:]:
    print(x)
