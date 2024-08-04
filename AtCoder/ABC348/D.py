from collections import deque


H, W = map(int, input().split())
A = ["#" * (W + 2)] + ["#" + input() + "#" for _ in range(H)] + ["#" * (W + 2)]
N = int(input())
RCE = [tuple(map(int, input().split())) for _ in range(N)]

B = [[-1] * (W + 2) for _ in range(H + 2)]
for i, (r, c, e) in enumerate(RCE):
    B[r][c] = i


for h in range(1, H + 1):
    for w, c in enumerate(A[h]):
        if c == "S":
            S = B[h][w]
            if S == -1:
                print("No")
                exit()
        if c == "T":
            B[h][w] = N

E = [[] for _ in range(N + 1)]

visited = [[-1] * (W + 2) for _ in range(H + 2)]
for i, (h0, w0, e0) in enumerate(RCE):
    queue = deque([(h0, w0, e0)])

    while queue:
        h, w, e = queue.popleft()
        if visited[h][w] == i or A[h][w] == "#":
            continue
        visited[h][w] = i

        # print((h0, w0), (h, w))

        b = B[h][w]
        if b != -1:
            E[i].append(b)
            # print((i, b))

        if e == 0:
            continue

        queue.append((h + 1, w, e - 1))
        queue.append((h - 1, w, e - 1))
        queue.append((h, w + 1, e - 1))
        queue.append((h, w - 1, e - 1))

queue = deque([S])
visited = [False] * (N + 1)
while queue:
    q = queue.popleft()
    if visited[q]:
        continue
    visited[q] = True

    for e in E[q]:
        queue.append(e)

print("Yes" if visited[N] else "No")
