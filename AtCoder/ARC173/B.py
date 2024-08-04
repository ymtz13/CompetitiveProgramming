N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

maxcnt = 0
for i, (x1, y1) in enumerate(P):
    for j, (x2, y2) in enumerate(P[i + 1 :], i + 1):
        cnt = 0
        for x, y in P:
            dx1 = x1 - x
            dy1 = y1 - y
            dx2 = x2 - x
            dy2 = y2 - y

            if dx1 * dy2 - dx2 * dy1 == 0:
                cnt += 1

        # print((i, j), cnt)
        maxcnt = max(maxcnt, cnt)

p = N - maxcnt

print(min(p, N // 3))
