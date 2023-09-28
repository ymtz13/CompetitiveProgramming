N = input()

p = 10
for d in N:
  d = int(d)
  if d >= p:
    print('No')
    exit()
  p = d

print('Yes')