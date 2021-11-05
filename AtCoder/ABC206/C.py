from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

D = defaultdict(int)
for a in A:
  D[a] += 1

ans = 0
for a in D:
  ans += D[a]*(N-D[a])

ans //= 2
print(ans)
