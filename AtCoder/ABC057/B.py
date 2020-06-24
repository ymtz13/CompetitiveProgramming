N, M = list(map(int, input().split()))
S = [tuple(map(int, input().split())) for _ in range(N)]
P = [tuple(map(int, input().split())) for _ in range(M)]

for sx, sy in S:
    m = 10**9
    for i, (px, py) in enumerate(P):
        d = abs(px-sx)+abs(py-sy)
        if d<m:
            im = i
            m = d
    print(im+1)
