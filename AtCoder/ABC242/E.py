mod = 998244353

T = int(input())
ans = []

for _ in range(T):
  N = int(input())
  S = input()
  M = (N + 1) // 2
  T = [None] * N

  a = 0
  for i, c in enumerate(S[:M]):
    T[i] = T[-1 - i] = c
    c = ord(c) - ord('A')
    a += c * pow(26, M - i - 1, mod)
    a %= mod

  T = ''.join(T)
  if T <= S: a += 1

  ans.append(a % mod)

for a in ans:
  print(a)
