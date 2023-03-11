from string import ascii_lowercase

ascii_lowercase = 'abc'
nchar = len(ascii_lowercase)

A = input()
N = len(A)

S = set()
K = [N]
for i in range(N - 1, -1, -1):
  a = A[i]
  S.add(a)
  if len(S) == nchar:
    K.append(i)
    S = set()

K = K[::-1]

ans = []

x = 0
for i in range(len(K)):
  k = K[i]
  s = {a for a in A[x:k]}

  for c in ascii_lowercase:
    if c not in s: break
  print(i, A[x:k], s, c)

  ans.append(c)
  if i == len(K) - 1: break

  for z in range(k, K[i + 1]):
    if A[z] == c: break

  x = z + 1

#solve(A, K, 0)

print(''.join(ans))
