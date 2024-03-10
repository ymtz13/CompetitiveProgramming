H, W, N = map(int, input().split())
A = [[0] * W for _ in range(H)]

h = w = 0
dh = -1
dw = 0

for _ in range(N):
    a = A[h][w]
    if a:
        A[h][w] = 0
        dh, dw = -dw, dh
    else:
        A[h][w] = 1
        dh, dw = dw, -dh

    h += dh
    w += dw
    h %= H
    w %= W

for row in A:
    row = ["#" if a else "." for a in row]
    print("".join(row))
