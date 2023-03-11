N = int(input())
LR = sorted([tuple(map(int, input().split())) for _ in range(N)])

ans = []
L, R = LR[0]
for l, r in LR[1:]:
  if l > R:
    ans.append((L, R))
    L, R = l, r
  
  else:
    R = max(R, r)

ans.append((L, R))

for l, r in ans:
  print(l, r)
