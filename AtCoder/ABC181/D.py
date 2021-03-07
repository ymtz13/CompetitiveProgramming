S = input()

if len(S)==1:
  print('Yes' if S=='8' else 'No')
  exit()

if len(S)==2:
  print('Yes' if int(S)%8==0 or int(S[::-1])%8==0 else 'No')
  exit()

N = [0]*10
for c in S: N[int(c)]+=1

for x in range(8, 1000, 8):
  x = '{:03d}'.format(x)
  ok = True
  for i in range(10):
    if N[i]<x.count(str(i)): ok=False
  if ok: break

print('Yes' if ok else 'No')