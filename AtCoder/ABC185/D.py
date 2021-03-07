N, M = map(int, input().split())
A = sorted(list(map(int, input().split())) + [N+1])
x = 0
D = []
for a in A:
  l = a-x-1
  if l>0: D.append(a-x-1)
  x = a

if len(D)==0:
  print(0)
  exit()

l = min(D)
ans = sum([(d+l-1)//l for d in D])
print(ans)
