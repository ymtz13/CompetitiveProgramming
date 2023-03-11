S = input()
ans = 0
for c in 'atcoder':
  ans += S.find(c)
  S = S.replace(c, '')

print(ans)
