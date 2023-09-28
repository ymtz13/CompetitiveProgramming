N = int(input())
X = [[0] * 105 for _ in range(105)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    for x in range(A, B):
        for y in range(C, D):
            X[x][y] = 1

ans = sum([sum(row) for row in X])
print(ans)
