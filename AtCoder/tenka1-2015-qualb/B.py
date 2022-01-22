S = input()

ans = 'set'
if S == '{}': ans = 'dict'

x = 0
for c in S:
  if c == '{': x += 1
  if c == '}': x -= 1
  if x == 1 and c == ':':
    ans = 'dict'

print(ans)
