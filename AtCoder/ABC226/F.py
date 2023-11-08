primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
lcms = []


def dfs(i, s, r, d):
    if s > 50:
        return
    if i == len(primes):
        lcms.append(r)
        return

    p = primes[i]

    for n in range(8):
        q = p**n
        dfs(i + 1, s + q, r * q, d * (n + 1))


dfs(0, 0, 1, 1)
lcms.sort()
print(lcms)

mod = 998244353

F = [1]
for i in range(1, 100):
    F.append(F[-1] * i % mod)

N, K = map(int, input().split())

for lcm in lcms:
    dividers = [d for d in range(1, lcm + 1) if lcm % d == 0]
