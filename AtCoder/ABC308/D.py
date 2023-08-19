from collections import deque

H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2

S = ["." * W2] + ["." + input() + "." for _ in range(H)] + ["." * W2]


M = H2 * W2
visited = [False] * M
queue = deque([W2 + 1])
snuke = "snuke"

while queue:
    q = queue.popleft()
    i = q // M
    hw = q % M
    if visited[hw]:
        continue

    h = hw // W2
    w = hw % W2
    if snuke[i] != S[h][w]:
        continue

    visited[hw] = True

    inext = (i + 1) % 5

    # print(h, w, snuke[i])
    queue.append(inext * M + hw - 1)
    queue.append(inext * M + hw + 1)
    queue.append(inext * M + hw - W2)
    queue.append(inext * M + hw + W2)

print("Yes" if visited[M - 2 - W2] else "No")
