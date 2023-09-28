W, H, N = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

x0, y0 = XY[0]
ans = 0
for xi, yi in XY[1:]:
    dx = xi - x0
    dy = yi - y0
    x0 = xi
    y0 = yi

    if dx > 0 and dy > 0:
        m = min(dx, dy)
        dx -= m
        dy -= m
        ans += m

    if dx < 0 and dy < 0:
        m = max(dx, dy)
        dx -= m
        dy -= m
        ans += -m

    ans += abs(dx) + abs(dy)


print(ans)
