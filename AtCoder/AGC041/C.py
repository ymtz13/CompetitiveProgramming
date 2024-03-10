orda = ord("a")

N = int(input())
A = [[ord(".")] * N for _ in range(N)]

L = "L"
R = "R"
U = "U"
D = "D"


def put(h, w, d):
    mh = h % 4
    mw = w % 4
    i = mh * 4 + mw + orda

    A[h][w] = i

    if d == L:
        A[h][w - 1] = i
    if d == R:
        A[h][w + 1] = i
    if d == U:
        A[h - 1][w] = i
    if d == D:
        A[h + 1][w] = i


def put1(h, w):
    put(h, w, D)
    put(h + 2, w + 1, R)


def put2(h, w):
    put(h, w, D)
    put(h + 1, w + 2, D)
    put(h, w + 1, R)
    put(h + 2, w, R)


def square(h, w, k, q):
    for m in range(k):
        x = min(2, q)
        q -= x

        for ih in range(k):
            iw = (ih + m) % k
            if x == 1:
                put1(h + ih * 3, w + iw * 3)
            if x == 2:
                put2(h + ih * 3, w + iw * 3)


if N == 2:
    print(-1)
    exit()

elif N == 3:
    put1(0, 0)

elif N == 4:
    put(0, 0, R)
    put(1, 0, R)
    put(2, 2, R)
    put(3, 2, R)
    put(0, 2, D)
    put(0, 3, D)
    put(2, 0, D)
    put(2, 1, D)

elif N % 5 == 0:
    for i in range(0, N, 5):
        put(i + 0, i + 0, R)
        put(i + 0, i + 2, R)
        put(i + 0, i + 4, D)
        put(i + 2, i + 4, D)
        put(i + 4, i + 4, L)
        put(i + 4, i + 2, L)
        put(i + 4, i + 0, U)
        put(i + 2, i + 0, U)
        put1(i + 1, i + 1)

elif N == 11:
    square(1, 1, 3, 4)
    for i in range(5):
        put(0, i * 2, R)
        put(i * 2, 10, D)
        put(10, 10 - i * 2, L)
        put(10 - i * 2, 0, U)

else:
    q = (N // 6) * 3
    square(0, 0, (N // 6) * 2, q - N % 6)
    for i in range(0, q * 2, 2):
        for j in range(1, N % 6 + 1):
            put(N - j, i, R)
            put(i, N - j, D)


for row in A:
    print("".join(map(chr, row)))
