from math import gcd


def solve(n):
    for m in range(2, 1000000):
        g = gcd(n, m)
        n //= g

        if n == 1:
            return m

    return n


n = int(input())
# print(solve(n))

for i in range(2, 20000):
    print(i, solve(i))
