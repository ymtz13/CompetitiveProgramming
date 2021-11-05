N = input()
if len(N)==1:
  print('Yes')
  exit()

for i, c in enumerate(N[::-1]):
  if c!='0': break

N = '0'*i + N

ans = 'Yes'
for i in range(len(N)):
  if N[i] != N[-i-1]: ans = 'No'

print(ans)
