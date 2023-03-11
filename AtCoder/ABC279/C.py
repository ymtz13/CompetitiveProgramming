H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

St = [''.join(c) for c in zip(*S)]
Tt = [''.join(c) for c in zip(*T)]

St.sort()
Tt.sort()

ans = 'Yes'
for s, t in zip(St, Tt):
  if s != t: ans = 'No'

print(ans)
