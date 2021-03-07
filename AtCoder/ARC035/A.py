s = input()
ans = 'YES'
for cf, cb in zip(s, s[::-1]):
  if cf!='*' and cb!='*' and cf!=cb: ans = 'NO'
print(ans)
