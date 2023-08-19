N = int(input())

base1 = list(range(1, N + 1))
base2 = base1[::-1]
base2[0] = N - 1
base2[1] = N

A = list(map(int, input().split()))
B = A[:]

odd = N % 2 == 1
even = not odd

ans = []

if even and sum(A) % N:
  ans.append(base1[:])
  for i, v in enumerate(base1):
    A[i] += v

S = sum(A)
if S % N != 0:
  print('No')
  exit()

print('Yes')

T = S // N

Aov = []
Alw = []
for i, a in enumerate(A):
  d = a - T
  if d > 0:
    Aov.extend([i] * d)
  else:
    Alw.extend([i] * (-d))

idx = set(range(N))

for aov, alw in zip(Aov, Alw):
  idxR = idx - {aov, alw}
  ii = [aov, alw] + list(idxR)

  op1 = [None] * N
  op2 = [None] * N

  for j, i in enumerate(ii):
    op1[i] = base1[j]
    op2[i] = base2[j]

  ans.append(op1)
  ans.append(op2)

print(len(ans))
for a in ans:
  print(*a)

  for i, v in enumerate(a):
    B[i] += v

# print(len(ans))
# print(B)
