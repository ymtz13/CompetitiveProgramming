N = int(input())
S = list(map(int, input().split()))

D = [S[i + 1] - S[i] for i in range(N - 1)]

DD = [D[i::3] for i in range(3)]

M = []
for dd in DD:
  m = x = 0
  for d in dd:
    x += d
    m = min(m, x)

  M.append(m)

#print(M)

A = [-M[0], -M[1]]
A.append(S[0] - sum(A))
#print(A)

if A[2] < -M[2]:
  print('No')
  exit()

for i in range(3, N + 2):
  A.append(A[i - 3] + D[i - 3])

print('Yes')
print(' '.join(map(str, A)))
