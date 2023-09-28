H, W = map(int, input().split())
S = [input() for _ in range(H)]
C = [[9] * W for _ in range(H)]
L = []

for h, row in enumerate(S):
    for w, c in enumerate(row):
        if c == ".":
            continue

        cnt = int(c)
        for dh in (-1, 0, 1):
            for dw in (-1, 0, 1):
                hh = h + dh
                ww = w + dw
                if S[hh][ww] == ".":
                    cnt -= 1
        C[h][w] = cnt

        if cnt <= 0:
            L.append((h, w))

ans = 0
while L:
    ans += 1
    L_next = []

    for h, w in L:
        for dh in (-1, 0, 1):
            for dw in (-1, 0, 1):
                hh = h + dh
                ww = w + dw
                C[hh][ww] -= 1
                if C[hh][ww] == 0:
                    L_next.append((hh, ww))

    L = L_next

print(ans)
