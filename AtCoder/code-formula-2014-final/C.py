S = input() + ' '
U = set()
f = False
n = ''
for c in S:
  if f:
    if c in ' @':
      U.add(n)
      f = False
    n += c
  
  if c=='@':
    f = True
    n = ''

ans = sorted(list(U - {''}))
for a in ans:
  print(a)