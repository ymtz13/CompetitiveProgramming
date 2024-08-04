N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
D = set([(b - a) % N for a, b in AB])

E = [e for e in range(N) if e not in D]

X = list(D) + E[: M - len(D)]

ans = []
for x in X:
    for i in range(N):
        j = (i + x) % N
        ans.append((i, j))

print(len(ans))
for i, j in ans:
    print(i + 1, j + 1)
