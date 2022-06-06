N = int(input())
P = set()

ans = None
m = -1
for n in range(N):
  S, T = input().split()
  T = int(T)

  if S in P: continue
  P.add(S)

  if T > m:
    ans = n + 1
    m = T

print(ans)
