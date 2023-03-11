N, M = map(int, input().split())
A = list(map(int, input().split()))

M3 = M * 3
X = [[] for _ in range(M3)]

S = 0
for i in range(N - 1):
  f, t = A[i] - 1, A[i + 1] - 1

  if f < t:
    X[f].append(t)
    X[f + M].append(t + M)
    X[f + M * 2].append(t + M * 2)
    S += t - f

  else:
    X[f].append(t + M)
    X[f + M].append(t + M * 2)
    S += t + M - f

Zcnt = [0] * M3
Zs = [0] * M3

cnt = 0
s = 0
ans = 1 << 60
for i in range(M3):
  a = S + s - cnt * (i - 1)
  ans = min(ans, a)

  cnt -= Zcnt[i]
  s -= Zs[i]

  for x in X[i]:
    cnt += 1
    s += i
    Zcnt[x] += 1
    Zs[x] += i

print(ans)
