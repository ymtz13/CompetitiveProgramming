from collections import deque

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0
queue = deque([(0, 0, {A[0][0]})])
while queue:
    h, w, a = queue.popleft()

    if h == H - 1 and w == W - 1:
        if len(a) == H + W - 1:
            ans += 1
        continue

    if h < H - 1:
        hh = h + 1
        queue.append((hh, w, a | {A[hh][w]}))

    if w < W - 1:
        ww = w + 1
        queue.append((h, ww, a | {A[h][ww]}))

print(ans)
