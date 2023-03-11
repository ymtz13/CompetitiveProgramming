N = int(input())
H = list(map(int, input().split()))

M = max(H)
for i, h in enumerate(H, 1):
  if h == M:
    print(i)
