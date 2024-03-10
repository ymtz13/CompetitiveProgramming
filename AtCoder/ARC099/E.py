from collections import deque

N, M = map(int, input().split())
E = [set([i for i in range(N) if i != j]) for j in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    E[A].remove(B)
    E[B].remove(A)

dp = [0] * (N + 1)
dp[0] = 1

dist = [-1] * N
for st in range(N):
    if dist[st] != -1:
        continue

    queue = deque([st * 2])
    n = [0] * 2
    while queue:
        q = queue.popleft()
        i = q // 2
        d = q % 2

        if dist[i] != -1:
            if dist[i] != d:
                print(-1)
                exit()
            continue

        dist[i] = d
        n[d] += 1

        for j in E[i]:
            queue.append(j * 2 + 1 - d)

    dp_next = [0] * (N + 1)
    for c, v in enumerate(dp):
        if not v:
            continue

        c0 = c + n[0]
        c1 = c + n[1]

        if c0 <= N:
            dp_next[c0] = 1
        if c1 <= N:
            dp_next[c1] = 1

    dp = dp_next

ans = M + 1
for c0, v in enumerate(dp):
    if not v:
        continue

    c1 = N - c0
    ans = min(ans, c0 * (c0 - 1) // 2 + c1 * (c1 - 1) // 2)

print(ans)
