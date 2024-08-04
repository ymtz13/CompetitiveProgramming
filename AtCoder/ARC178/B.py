mod = 998244353
inv2 = pow(2, mod - 2, mod)


def solve(A1, A2, A3):
    if max(A1, A2) != A3 and max(A1, A2) + 1 != A3:
        return 0

    if A1 < A2:
        A1, A2 = A2, A1

    z = pow(10, A2 - 1, mod)
    z9 = 9 * z % mod

    t1 = z9 * (z9 + 1) * inv2 % mod
    t2 = z9 * (z - 1) % mod

    if A1 == A2:
        t1 -= z * (z - 1) * inv2
        t1 %= mod

    ret = (t1 + t2) % mod
    ret %= mod

    if max(A1, A2) == A3:
        a = 9 * pow(10, A1 - 1, mod) * z9
        ret = (a - ret) % mod

    return ret


T = int(input())

for _ in range(T):
    A1, A2, A3 = map(int, input().split())
    print(solve(A1, A2, A3))
