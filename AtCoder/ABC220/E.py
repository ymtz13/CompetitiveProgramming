mod = 998244353
N, D = map(int, input().split())

B = [1]
for i in range(1, 3 * 10**6):
  B.append(B[-1] * 2 % mod)

ans = 0
for l in range(N):
  if l + D < N: c = (D + 3) * B[D - 1]
  if l + D == N: c = (D - 1) * B[D - 1]
  if l + D > N: c = max(0, -D + 2 * (N - l - 1) + 1) * B[D - 1]
  ans = (ans + c * B[l]) % mod

print(ans)
