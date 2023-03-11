N = int(input())
S = input()

ans = []
for i in range(1, N):
  a = 0
  for k in range(N - i):
    if S[k] == S[k + i]: break
    a += 1

  ans.append(a)

for a in ans:
  print(a)
