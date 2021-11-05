N = int(input())
A = list(map(int, input().split()))
X = int(input())

S = sum(A)
M = X // S
X -= M * S

c = 0
for i, a in enumerate(A):
  if X < 0: break
  c = i + 1
  X -= a

print(M * N + c)
