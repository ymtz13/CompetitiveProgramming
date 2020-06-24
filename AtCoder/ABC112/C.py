l_bound = [[1]*101 for _ in range(101)]
u_bound = [[10**9]*101 for _ in range(101)]

N = int(input())
for n in range(N):
    x, y, h = list(map(int, input().split()))

    if h==0:
        for r in range(101):
            for c in range(101):
                u_bound[r][c] = min(u_bound[r][c], abs(c-x) + abs(r-y))
    else:
        for r in range(101):
            for c in range(101):
                l_bound[r][c] = max(l_bound[r][c], h + abs(c-x) + abs(r-y))
                u_bound[r][c] = min(u_bound[r][c], h + abs(c-x) + abs(r-y))

for r in range(101):
    for c in range(101):
        if l_bound[r][c] == u_bound[r][c]:
            print(c, r, l_bound[r][c])
