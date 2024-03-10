mod = 998244353

N = int(input())
X = list(map(int, input()))

s = 1
p = 0
for i, x in enumerate(reversed(X)):
    p += x * s
    p %= mod

    s = 10 * s + p
    s %= mod

print(p % mod)
