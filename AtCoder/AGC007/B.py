N = int(input())
P = list(map(int, input().split()))
Q = [None] * N
for q, p in enumerate(P):
  Q[p - 1] = q

D = [Q[0]]

for p in range(1, N):
  D.append(Q[p] - Q[p - 1])

a = b = 0
A = []
B = []
for d in D:
  if d >= 0:
    da = d + 1
    db = 1
  else:
    da = 1
    db = -d + 1

  a += da
  b -= db
  A.append(a)
  B.append(b)

M = -B[-1]
A = [a + M + 1 for a in A]
B = [b + M + 1 for b in B]

print(' '.join(map(str, A)))
print(' '.join(map(str, B)))
