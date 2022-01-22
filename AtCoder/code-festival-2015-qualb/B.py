N, M = map(int, input().split())
A = list(map(int, input().split()))
C = [0] * (M + 1)
for a in A:
  C[a] += 1

ans = '?'
for i, c in enumerate(C):
  if c * 2 > N: ans = i

print(ans)