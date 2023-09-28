N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
S = set(P)

ans = 0
for i, (x0, y0) in enumerate(P):
    for x1, y1 in P[i + 1 :]:
        dx = x1 - x0
        dy = y1 - y0

        ex = dy
        ey = -dx

        fx = dx + ex
        fy = dy + ey

        if fx % 2 or fy % 2:
            continue

        x2 = x0 + fx // 2
        y2 = y0 + fy // 2

        x3 = x0 - x2 + x1
        y3 = y0 - y2 + y1

        if (x2, y2) in S and (x3, y3) in S:
            ans = max(ans, (fx * fx + fy * fy) // 4)

print(ans)
