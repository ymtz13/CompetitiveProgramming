N, M, A, B = map(int, input().split())
X = [0] + [max(A, B)] * N
for _ in range(M):
    L, R = map(int, input().split())
    for i in range(L, R + 1):
        X[i] = A

print(sum(X))
