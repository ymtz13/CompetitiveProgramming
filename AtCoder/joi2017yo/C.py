N, M, D = map(int, input().split())
X = [input() for _ in range(N)]

ans = 0

if D <= N:
    for m in range(M):
        for n in range(N - D + 1):
            ok = True
            for i in range(D):
                if X[n + i][m] == "#":
                    ok = False
            if ok:
                ans += 1

if D <= M:
    for m in range(M - D + 1):
        for n in range(N):
            ok = True
            for i in range(D):
                if X[n][m + i] == "#":
                    ok = False
            if ok:
                ans += 1

print(ans)
