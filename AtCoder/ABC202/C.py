N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

Bi = [[] for _ in range(N+1)] # Bi[x] := { i | B[i]==x }
for i, x in enumerate(B):
  Bi[x].append(i+1)

Cc = [0]*(N+1)
for c in C:
  Cc[c] += 1

memo = [None]*(N+1)

ans = 0
for a in A:
  if memo[a] is not None:
    ans += memo[a]
    continue

  v = 0
  for i in Bi[a]:
    v += Cc[i]

  ans += v
  memo[a] = v

print(ans)
