N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
S = -sum([A for A, B in AB])
D = sorted([A*2+B for A, B in AB], reverse=True)

ans = 0
for d in D:
  if S<=0: ans += 1
  S += d

print(ans)