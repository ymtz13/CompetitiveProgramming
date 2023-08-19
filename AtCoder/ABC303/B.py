N, M = map(int, input().split())
ans = [[True] * N for _ in range(N)]

for _ in range(M):
    A = list(map(int, input().split()))
    for v1, v2 in zip(A, A[1:]):
        ans[v1 - 1][v2 - 1] = ans[v2 - 1][v1 - 1] = False

x = []
for i in range(N):
    for j in range(i + 1, N):
        if ans[i][j]:
            x.append((i + 1, j + 1))

print(len(x))
