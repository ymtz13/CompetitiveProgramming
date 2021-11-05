from collections import defaultdict

K = int(input())
D = defaultdict(int)
for p in range(2, 10**6+10):
  while K%p==0:
    K//=p
    D[p] += 1

if K>1: D[K] += 1


def comb3(n): return (n+2)*(n+1)//2
ans = 1
for v in D.values(): ans *= comb3(v)

n3 = 1 if all([v%3==0 for v in D.values()]) else 0

n2 = 1
for v in D.values(): n2 *= v//2+1

print((ans + n3*6 + (n2-n3)*3)//6)
