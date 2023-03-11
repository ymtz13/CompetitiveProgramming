T = int(input())
ans = []

for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))

  a = 0
  for x in A:
    if x % 2 == 1: a += 1

  ans.append(a)

for a in ans:
  print(a)
