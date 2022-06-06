from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

DA = defaultdict(int)
DB = defaultdict(int)
for a in A:
  DA[a] += 1
for b in B:
  DB[b] += 1

for i in DB:
  if DA[i] < DB[i]:
    print('No')
    exit()

print('Yes')
