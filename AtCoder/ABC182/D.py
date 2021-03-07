N = int(input())
A = list(map(int, input().split()))

X = []
S = []
x = s = 0
for a in A:
  x += a
  s = max(s, x)
  X.append(x)
  S.append(s)

ans = 0
z = 0
for x, s in zip(X, S):
  ans = max(ans, z+s)
  z += x

print(ans)