from collections import defaultdict

N = int(input())
D = defaultdict(int)

ans = []
for _ in range(N):
  S = input()

  if S in D:
    ans.append(S + '({})'.format(D[S]))
  else:
    ans.append(S)

  D[S] += 1

for a in ans:
  print(a)
