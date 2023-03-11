N, M = map(int, input().split())
S = [input()[-3:] for _ in range(N)]
T = {input() for _ in range(M)}

ans = 0
for s in S:
  if s in T: ans += 1

print(ans)
