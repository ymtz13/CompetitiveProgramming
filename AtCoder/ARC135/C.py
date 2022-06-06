N = int(input())
A = list(map(int, input().split()))

C = [0] * 32
X = [1 << i for i in range(32)]

for a in A:
  for i in range(32):
    if a & (1 << i): C[i] += 1

ans = 0
for a in A + [0]:
  s = 0
  
  for c, x in zip(C, X):
    if a & x:
      s += (N - c) * x
    else:
      s += c * x
    
  ans = max(ans, s)

print(ans)
