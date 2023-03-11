N = int(input())
S = input()

f = False
ans = []
for c in S:
  if c == '"': f = not f
  if c == ',' and not f: c = '.'
  ans.append(c)

print(''.join(ans))
