mod = 998244353

N = int(input())
A = list(map(int, input()))
B = list(map(int, input()))

for i, (a, b) in enumerate(zip(A, B)):
  if a < b:
    A[i] = b
    B[i] = a

r = 0
p = 1
for a in reversed(A):
  r += p * a % mod
  r %= mod

  p = p * 10 % mod

ans = 0
p = 1
for b in reversed(B):
  ans += r * p * b % mod
  ans %= mod
  p = p * 10 % mod

print(ans)
