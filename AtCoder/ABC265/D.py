N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0]
for a in A:
  S.append(S[-1] + a)

X = set(S)

Y = set()
for s in S:
  if s - P in X: Y.add(s)

Z = set()
for s in S:
  if s - Q in Y: Z.add(s)

W = set()
for s in S:
  if s - R in Z: W.add(s)

print('Yes' if W else 'No')
