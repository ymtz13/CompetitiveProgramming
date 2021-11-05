N = int(input())
ans = 0
for k in range(100):
  if 2**k > N: break
  ans = k
print(ans)
