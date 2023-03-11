H, W = map(int, input().split())
ans = [0] * W
for _ in range(H):
  for i, c in enumerate(input()):
    if c == '#': ans[i] += 1

print(' '.join(map(str, ans)))
