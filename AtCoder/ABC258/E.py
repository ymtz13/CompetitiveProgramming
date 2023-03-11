N, Q, X = map(int, input().split())
W = list(map(int, input().split()))

S = [0]
for w in W:
  S.append(S[-1] + w)


def f(i):
  R = S[-1] - S[i]
  if R >= X:
    ok = N - 1
    ng = i - 1
    while ok - ng > 1:
      tgt = (ok + ng) // 2
      if S[tgt + 1] - S[i] >= X:
        ok = tgt
      else:
        ng = tgt

    return (ok - i + 1), (ok + 1) % N

  else:
    D = X - R
    cnt = N - i

    cnt += (D // S[-1]) * N
    D %= S[-1]

    if D == 0: return cnt, 0

    ok = N - 1
    ng = -1
    while ok - ng > 1:
      tgt = (ok + ng) // 2
      if S[tgt + 1] >= D:
        ok = tgt
      else:
        ng = tgt

    return cnt + ok + 1, (ok + 1) % N


C = []
visited = [None] * N
i = 0
v = 0

while visited[i] is None:
  visited[i] = v
  v += 1
  cnt, i = f(i)

  C.append(cnt)

p = visited[i]
q = v - p

ans = []

for _ in range(Q):
  K = int(input())
  K -= 1

  if K < p:
    ans.append(C[K])
  else:
    ans.append(C[p + (K - p) % q])

for a in ans:
  print(a)
