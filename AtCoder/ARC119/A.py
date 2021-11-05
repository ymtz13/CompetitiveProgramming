N = int(input())
ans = N
for b in range(100):
  d = 1 << b
  if d > N: break
  a, c = N//d, N%d
  ans = min(ans, a+b+c)
print(ans)
