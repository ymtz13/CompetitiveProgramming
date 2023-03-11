mod = 998244353

N = tuple(map(int, input()))
M = int(input())
C = tuple(map(int, input().split()))

L = len(N)

P = [0]
for _ in range(L):
  P.append((P[-1] * 10 + 1) % mod)

ans = 0
#for b in range(1 << M):
for b in range(1):
  D = {c for i, c in enumerate(C) if b & (1 << i)}
  E = set(range(10)) - D
  R = sum(E)
  K = len(E)

  # 1~Nの数で、Dに含まれる数字を含まないものの総和
  S = 1
  for i, n in enumerate(N):
    r = L - i - 1

    Ei = [v for v in E if 0 < v < n]
    Ri = sum(Ei)
    Ki = len(Ei)

    s = 0
    if r > 0: s = R * P[r] * pow(K, r - 1, mod) * Ki % mod
    s += sum() * pow(10, r, mod) * pow(K, r, mod)

    S += s

    if n in D:
      S -= 1
      break

  ans += (-1)**len(D) * S

print(ans)
