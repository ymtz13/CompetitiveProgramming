N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for i in range(N):
  for j in range(i + 1, N):
    ok = True
    for ci, cj in zip(S[i], S[j]):
      if ci == 'x' and cj == 'x': ok = False
    if ok: ans += 1

print(ans)
