def parse(s):
  r = 0
  b = 1
  for c in s:
    r += b*int(c)
    b *= 8
  return r

def tostr(x):
  r = []
  while x:
    r.append(x%9)
    x//=9
  return r

N, K = map(int, input().split())
b8 = [int(c) for c in str(N)][::-1]

for _ in range(K):
  xx = parse(b8)
  b9 = tostr(xx)  
  b8 = list(map(lambda v: 5 if v==8 else v, b9))

print(''.join(map(str, b8[::-1])) if b8 else 0)
