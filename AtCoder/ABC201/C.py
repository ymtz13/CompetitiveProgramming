S = input()

ans = 0
for X in range(10000):
  T = set(map(int, '{:04d}'.format(X)))

  ok = True
  for d in range(10):
    if S[d]=='o' and d not in T:
      ok = False
      break
    
    if S[d]=='x' and d in T:
      ok = False
      break
  
  if ok: ans += 1

print(ans)
