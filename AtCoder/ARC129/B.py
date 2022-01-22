N = int(input())

minR = 1 << 30
maxL = 0

for _ in range(N):
  L, R = map(int, input().split())

  minR = min(minR, R)
  maxL = max(maxL, L)

  if maxL <= minR:
    print(0)
  else:
    print((maxL - minR + 1) // 2)
