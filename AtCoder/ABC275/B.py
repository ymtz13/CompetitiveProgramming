mod = 998244353
A, B, C, D, E, F = map(int, input().split())
print((A * B * C - D * E * F) % mod)
