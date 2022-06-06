from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
for a, b in zip(A, B):
  if a == b: ans1 += 1

DA = defaultdict(int)
for a in A:
  DA[a] += 1
DB = defaultdict(int)
for b in B:
  DB[b] += 1

ans2 = -ans1
for a in DA:
  ans2 += DA[a] * DB[a]

print(ans1)
print(ans2)
