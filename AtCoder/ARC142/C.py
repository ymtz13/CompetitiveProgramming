N = int(input())

ans = 10000
v12 = None
v21 = None

for m in range(3, N + 1):
  print('? 1 {}'.format(m))
  d1m = int(input())
  print('? 2 {}'.format(m))
  d2m = int(input())
  ans = min(ans, d1m + d2m)

  if d1m == 1 and d2m == 2: v12 = m
  if d1m == 2 and d2m == 1: v21 = m

if ans == 3:
  if v12 is None or v21 is None:
    ans = 1
  
  else:
    print('? {} {}'.format(v12, v21))
    d = int(input())
    if d > 2:
      ans = 1

print('!', ans)
