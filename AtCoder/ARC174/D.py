from math import isqrt


def naive(N):
    sety = set()
    cnt = 0
    for x in range(1, N + 1):
        y = isqrt(x)

        sx = str(x)
        sy = str(y)
        if sx[: len(sy)] == sy:
            cnt += 1
            # print(x, y)
            sety.add(y)
    return cnt


Z = [1, 80] + list(range(90, 100))


def solve(N):
    if N < 100:
        return len([t for t in Z if t <= N])

    s = len(Z)
    for y in range(1, 10):
        # 1[0..0][X..X]
        l = 10 ** (y * 2)
        r = l + (10**y)
        if N < l:
            break
        s += min(r, N + 1) - l

        # 9[9..8][0..0]
        v = int("9" * y + "8" + "0" * (y + 1))
        if N < v:
            break
        s += 1

        # 9[9..9][X..X]
        l = int("9" * (y + 1) + "0" * (y + 1))
        r = int("9" * (y + 1) + "9" * (y + 1)) + 1
        if N < l:
            break
        s += min(r, N + 1) - l

    return s


# for x in range(20000):
#     print(x)
#     nai = naive(x)
#     sol = solve(x)
#     assert nai == sol, (x, nai, sol)


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    a = solve(N)
    ans.append(a)

for a in ans:
    print(a)
