N = int(input())
B = []
for k in range(N):
  f = 1<<k
  x = False
  b = 0
  for i in range(1<<N):
    if i%f==0: x = not x
    if x: b += 1<<i
  B.append(b)

print((1<<N)-1)
for f in range(1, 1<<N):
  x = 0
  for i, b in enumerate(B):
    if f&(1<<i): x ^= b
  
  template = '{' + ':0{:}b'.format(1<<N) + '}'
  print(template.format(x).replace('0','A').replace('1','B'))

