from collections import deque

N, M = map(int, input().split())
S = [input() for _ in range(N)]


ans = [False] * (N * M)
visited = [False] * (N * M)
queue = deque([M + 1])

while queue:
    q = queue.popleft()
    if visited[q]:
        continue
    visited[q] = True
    ans[q] = True

    h = q // M
    w = q % M
    if S[h][w] == "#":
        continue

    # R
    for ww in range(w + 1, M):
        if S[h][ww] == "#":
            break
        ans[h * M + ww] = True
    queue.append(h * M + (ww - 1))

    # L
    for ww in range(w - 1, -1, -1):
        if S[h][ww] == "#":
            break
        ans[h * M + ww] = True
    queue.append(h * M + (ww + 1))

    # D
    for hh in range(h + 1, N):
        if S[hh][w] == "#":
            break
        ans[hh * M + w] = True
    queue.append((hh - 1) * M + w)

    # U
    for hh in range(h - 1, -1, -1):
        if S[hh][w] == "#":
            break
        ans[hh * M + w] = True
    queue.append((hh + 1) * M + w)

print(ans.count(True))
