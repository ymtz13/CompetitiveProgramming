N, K = map(int, input().split())
AB = sorted([tuple(map(int, input().split())) for _ in range(N)])

x = 0
for a, b in AB:
  need = a - x
  if need > K:
    print(x+K)
    exit()
  
  x = a
  K += b - need

print(x + K)
