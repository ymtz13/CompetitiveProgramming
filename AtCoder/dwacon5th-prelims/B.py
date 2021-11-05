N, K = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
for a in A:
  S.append(S[-1] + a)

X = []
for i, si in enumerate(S):
  for sj in S[:i]:
    X.append(si - sj)

ans = 0
for i in range(30, -1, -1):
  b = 1 << i
  F = list(filter(lambda x: x & b, X))
  if len(F) >= K:
    ans += b
    X = F

print(ans)
