N = int(input())
d = -N
p = 1
while p*p<N:
  if N%p==0: d += p + N//p
  p += 1
if p*p==N: d += p

print('Perfect' if d==N else 'Deficient' if d<N else 'Abundant')
