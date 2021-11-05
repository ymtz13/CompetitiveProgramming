A, B = map(int, input().split())
for T in range(1, 200001):
  a = (A+T-1)//T
  b = B//T
  if a<b: ans = T

print(ans)
