T = int(input())

ans = []
for _ in range(T):
  N = input()
  L = len(N)

  a = int('9' * (L - 1))

  for l in range(1, L):
    if L % l != 0: continue

    X = int(N[:l] * (L // l))
    if X <= int(N):
      a = max(a, X)
      continue

    X = int(str(int(N[:l]) - 1) * (L // l))
    if X <= int(N):
      a = max(a, X)
  
  ans.append(a)

for a in ans:
  print(a)
