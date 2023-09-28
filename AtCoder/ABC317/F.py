from itertools import product
from math import gcd

mod = 998244353

N, A1, A2, A3 = map(int, input().split())

A2A3 = A2 * A3
M = A1 * A2 * A3 * 27

MORE = 2
SAME = 1
LESS = 0


def encode(a1, a2, a3, c1, c2, c3):
    return 27 * (a1 * A2A3 + a2 * A3 + a3) + c1 * 9 + c2 * 3 + c3


def decode(code):
    a = code // 27
    c = code % 27

    a1 = a // A2A3
    ar = a % A2A3
    a2 = ar // A3
    a3 = ar % A3

    c1 = c // 9
    cr = c % 9
    c2 = cr // 3
    c3 = cr % 3

    return (a1, a2, a3, c1, c2, c3)


def compare(current, bit_N, bit_set):
    if bit_N < bit_set:
        return MORE
    if bit_N > bit_set:
        return LESS
    return current


dp = [0] * M
dp[encode(0, 0, 0, SAME, SAME, SAME)] = 1

for i in range(70):
    b = 1 << i

    bit_N = (N >> i) & 1

    dp_next = [0] * M

    for code_from, value_from in enumerate(dp):
        a1, a2, a3, c1, c2, c3 = decode(code_from)

        # 0, 0, 0
        code_to = encode(
            a1,
            a2,
            a3,
            compare(c1, bit_N, 0),
            compare(c2, bit_N, 0),
            compare(c3, bit_N, 0),
        )
        dp_next[code_to] += value_from
        dp_next[code_to] %= mod

        # 1, 1, 0
        code_to = encode(
            (a1 + b) % A1,
            (a2 + b) % A2,
            a3,
            compare(c1, bit_N, 1),
            compare(c2, bit_N, 1),
            compare(c3, bit_N, 0),
        )
        dp_next[code_to] += value_from
        dp_next[code_to] %= mod

        # 0, 1, 1
        code_to = encode(
            a1,
            (a2 + b) % A2,
            (a3 + b) % A3,
            compare(c1, bit_N, 0),
            compare(c2, bit_N, 1),
            compare(c3, bit_N, 1),
        )
        dp_next[code_to] += value_from
        dp_next[code_to] %= mod

        # 1, 0, 1
        code_to = encode(
            (a1 + b) % A1,
            a2,
            (a3 + b) % A3,
            compare(c1, bit_N, 1),
            compare(c2, bit_N, 0),
            compare(c3, bit_N, 1),
        )
        dp_next[code_to] += value_from
        dp_next[code_to] %= mod

    dp = dp_next

ans = -1
ans -= N // (A1 * A2 // gcd(A1, A2))
ans -= N // (A2 * A3 // gcd(A2, A3))
ans -= N // (A3 * A1 // gcd(A3, A1))

for c1, c2, c3 in product((SAME, LESS), repeat=3):
    ans += dp[encode(0, 0, 0, c1, c2, c3)]
    ans %= mod

print(ans)
