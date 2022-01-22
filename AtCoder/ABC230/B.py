T = 'oxx' * 100
S = input()
L = len(S)
ans = 'No'

for i in range(10):
  TT = T[i:i + L]
  if S==TT: ans = 'Yes'

print(ans)
