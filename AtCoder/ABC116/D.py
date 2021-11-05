from collections import deque

N, K = map(int, input().split())
X = [tuple(map(int, input().split())) for _ in range(N)]
X = sorted(X, key=lambda x: -x[1])

S = set()
R = []
p = 0
for t, d in X[:K]:
  p += d
  if t in S:
    R.append(d)
  else:
    S.add(t)

R = deque(sorted(R))

ans = p + len(S)**2

for t, d in X[K:]:
  if t in S: continue
  if not R: break
  S.add(t)
  p += d - R.popleft()
  ans = max(ans, p + len(S)**2)

print(ans)
