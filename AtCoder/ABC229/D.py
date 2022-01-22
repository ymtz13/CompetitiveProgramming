S = [0 if c == '.' else 1 for c in input()]
N = len(S)
K = int(input())

ans = 0
k = 0
t = -1
for s in range(N):
  if t < s - 1: t = s - 1
  while t + 1 < N and (S[t + 1] == 1 or k < K):
    t += 1
    if S[t] == 0:
      S[t] = 2
      k += 1

  ans = max(ans, t - s + 1)
  print(s, t, t - s + 1)
  print(S)
  print()

  if S[s] == 2:
    k -= 1
    S[s] = 0

print(ans)
