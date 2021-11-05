N = int(input())
S = input()
Q = int(input())
K = list(map(int, input().split()))

Sa = [0]
Sc = [0]
for c in S:
  Sa.append(Sa[-1])
  Sc.append(Sc[-1])
  if c == 'D': Sa[-1] += 1
  if c == 'C': Sc[-1] += 1

for k in K:
  x = 0
  ans = 0
  for i, c in enumerate(S):
    if c == 'D': x += Sc[min(N, i + k)] - Sc[i]
    if c == 'C': x -= Sa[i] - Sa[max(0, i - k + 1)]
    if c == 'M': ans += x

  print(ans)
