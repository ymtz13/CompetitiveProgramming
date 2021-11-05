N = int(input())
A = list(map(int, input().split()))

X = [-1] * 20
j = -1
ans = 0
for i, a in enumerate(A):
  for b, x in enumerate(X):
    if (a >> b) & 1:
      j = max(j, x)
      X[b] = i
  ans += i - j

print(ans)
