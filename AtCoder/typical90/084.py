N = int(input())
S = input()
cnt = 0

s = 0
for c in S+'_':
  if c=='o':
    s += 1
  else:
    cnt += s*(s+1)//2
    s = 0

s = 0
for c in S+'_':
  if c=='x':
    s += 1
  else:
    cnt += s*(s+1)//2
    s = 0

print(N*(N+1)//2 - cnt)
