from collections import defaultdict

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

Da = defaultdict(int)
for a in A: Da[a] += 1

ans = set()

for b in B:
  x = A[0] ^ b

  Db = defaultdict(int)
  for _b in B: Db[_b ^ x] += 1

  if Da==Db: ans.add(x)

ans = sorted(list(ans))
print(len(ans))
for a in ans:
  print(a)
