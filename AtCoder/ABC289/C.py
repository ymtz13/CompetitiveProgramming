N, M = map(int, input().split())

SS = []
for _ in range(M):
  input()
  S = set(map(int, input().split()))
  SS.append(S)

A = set(range(1, N + 1))

ans = 0
for i in range(1, 1 << M):
  ss = set()
  for j, s in enumerate(SS):
    if i & (1 << j):
      ss |= s

  if ss == A:
    ans += 1

print(ans)
