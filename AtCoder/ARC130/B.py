H, W, C, Q = map(int, input().split())
X = [tuple(map(int, input().split())) for _ in range(Q)]

T1 = set()
T2 = set()

ans = [0] * C

for t, n, c in reversed(X):
  if t == 1:
    if n in T1: continue
    T1.add(n)
    ans[c - 1] += W
    H -= 1

  else:
    if n in T2: continue
    T2.add(n)
    ans[c - 1] += H
    W -= 1

print(' '.join(map(str, ans)))
