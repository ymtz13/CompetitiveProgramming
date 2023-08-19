H, W, N = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

H1 = H + 1
W1 = W + 1
M = H1 * W1
Defect = [False] * M
Ch = [0] * M
Cw = [0] * M

for h in range(H1):
    P.append((h, 0))
for w in range(W1):
    P.append((0, w))

for a, b in P:
    i = a * W1 + b
    Defect[i] = True
    Ch[i] = a
    Cw[i] = b

ans = 0

for h in range(1, H1):
    for w in range(1, W1):
        i = h * W1 + w
        if Defect[i]:
            continue

        Ch[i] = ch = max(Ch[i - W1 - 1], Ch[i - W1])
        Cw[i] = cw = max(Cw[i - W1 - 1], Cw[i - 1])

        ans += min(h - ch, w - cw)

print(ans)
