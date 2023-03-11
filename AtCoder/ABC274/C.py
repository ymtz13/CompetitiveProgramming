N = int(input())
A = tuple(map(int, input().split()))

ans = [None, 0]
for i, a in enumerate(A, 1):
  g = ans[a]
  ans.append(g + 1)
  ans.append(g + 1)

for a in ans[1:]:
  print(a)
