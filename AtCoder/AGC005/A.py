X = input()
s = 0
ans = 0
for c in X:
  if c == 'T':
    if s == 0: ans += 2
    else: s -= 1
  else:
    s += 1

print(ans)
