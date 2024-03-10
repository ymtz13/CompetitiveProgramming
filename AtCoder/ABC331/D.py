N, Q = map(int, input().split())
P = [[1 if c == "B" else 0 for c in input()] for _ in range(N)]
Queries = [tuple(map(int, input().split())) for _ in range(Q)]


N2 = N
# M = [p + p for p in P]
# for m in M[:]:
#     M.append(m[:])
M = P

for i in range(N2):
    for j in range(N2 - 1):
        M[i][j + 1] += M[i][j]

for i in range(N2 - 1):
    for j in range(N2):
        M[i + 1][j] += M[i][j]


S = M[-1][-1]


def f(x, y):
    if x == -1 or y == -1:
        return 0

    mx = x % N
    my = y % N
    cx = x // N
    cy = y // N

    return cx * cy * S + M[mx][my] + M[-1][my] * cx + M[mx][-1] * cy


for x0, y0, x1, y1 in Queries:
    a = 0
    a += f(x1, y1)
    a -= f(x1, y0 - 1)
    a -= f(x0 - 1, y1)
    a += f(x0 - 1, y0 - 1)
    print(a)
