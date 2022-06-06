N = int(input())
C = [(c, i + 1) for i, c in enumerate(map(int, input().split()))]
C.sort()

V = [False] * (1 << 16)
V[0] = True

ans = 0
for c, k in C:
  if not V[k]:
    ans += c
    for i, v in enumerate(V):
      if v: V[i ^ k] = True

print(ans)
