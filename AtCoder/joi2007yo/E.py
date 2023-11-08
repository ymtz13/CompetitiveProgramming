a, b, c = map(int, input().split())
N = int(input())

X = [2] * (a + b + c + 1)

R0 = []
for _ in range(N):
    i, j, k, r = map(int, input().split())
    if r == 0:
        R0.append((i, j, k))
    else:
        X[i] = X[j] = X[k] = 1

for i, j, k in R0:
    if X[i] == 1 and X[j] == 1:
        X[k] = 0
    if X[j] == 1 and X[k] == 1:
        X[i] = 0
    if X[k] == 1 and X[i] == 1:
        X[j] = 0

for x in X[1:]:
    print(x)
