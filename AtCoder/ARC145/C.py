mod = 998244353

N = int(input())

F = [1]
for i in range(1, N * 2 + 10):
    F.append(F[-1] * i % mod)

cat = F[2 * N] * pow(F[N], mod - 3, mod) * pow(N + 1, mod - 2, mod) % mod

print(pow(2, N, mod) * F[N] * cat % mod)
