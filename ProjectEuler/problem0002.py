N = int(input())
F = [1, 1]
ans = 0
while True:
  v = sum(F[-2:])
  if v > N: break
  F.append(v)
  if v%2==0: ans += v

print(ans)
