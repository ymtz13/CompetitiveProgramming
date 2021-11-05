from collections import defaultdict

T = int(input())
for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  D = defaultdict(int)
  for a in A:
    D[a] += 1

  M = 0
  for d in D.values():
    if d % 2 == 1: M = 1
  
  print('First' if (N+M)%2==1 else 'Second')
