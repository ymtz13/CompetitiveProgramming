N, M = map(int, input().split())
X = [True] * (N + 1)
for _ in range(M):
    _, B = map(int, input().split())
    X[B] = False

ans = None
for i in range(1, N + 1):
    if X[i]:
        if ans is not None:
            print(-1)
            exit()
        ans = i

print(ans)
