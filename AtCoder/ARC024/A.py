input()
L = [0]*50
R = [0]*50
for s in map(int, input().split()):
  L[s] += 1
for s in map(int, input().split()):
  R[s] += 1

ans = 0
for l, r in zip(L, R):
  ans += min(l,r)
print(ans)