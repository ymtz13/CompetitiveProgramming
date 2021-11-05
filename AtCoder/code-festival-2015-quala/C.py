N, T = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

S = sum([a for a, _ in AB])
D = sorted([b - a for a, b in AB])

for n, d in enumerate(D + [0]):
  if S<=T:
    print(n)
    exit()
  S += d

print(-1)
