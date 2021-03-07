N, W = map(int, input().split())
M = 200010
X = [0]*M

for _ in range(N):
  S, T, P = map(int, input().split())
  X[S] += P
  X[T] -= P

Z = []
z = 0
for x in X:
  z += x
  Z.append(z)

print('Yes' if max(Z)<= W else 'No')
