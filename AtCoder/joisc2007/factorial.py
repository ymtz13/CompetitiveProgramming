from collections import defaultdict


def solve(n):
    nn = n

    factors = defaultdict(int)

    for p in range(2, 100000):
        while n % p == 0:
            factors[p] += 1
            n //= p

    if n > 1:
        factors[n] += 1

    def check(x):
        for f, c in factors.items():
            z = 1
            while z <= x:
                z *= f
                c -= x // z
                # print(f"x={x} f={f} c={c} z={z}")
            if c > 0:
                return False

        return True

    ok = nn
    ng = 1
    while ok - ng > 1:
        tgt = (ok + ng) // 2
        if check(tgt):
            ok = tgt
        else:
            ng = tgt

    return ok


n = int(input())
# print(solve(n))

for i in range(2, 20000):
    print(i, solve(i))
