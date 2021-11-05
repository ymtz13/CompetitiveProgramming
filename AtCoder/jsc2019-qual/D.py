N = int(input())

for i in range(N-1):
  ans = []
  for j in range(i + 1, N):
    for x in range(20):
      b = 1 << x
      if i & b != j & b:
        ans.append(x + 1)
        break
  print(' '.join(map(str, ans)))
