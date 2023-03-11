from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
C = defaultdict(int)

for a in A:
  C[a] += 1

C = list(C.items())
C.sort(reverse=True)

for k in range(N):
  ans = C[k][1] if k < len(C) else 0
  print(ans)
