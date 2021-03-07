from functools import cmp_to_key

N, A, B = map(int, input().split())
X = sorted([(int(a), 0) for a in input().split()])

if A==1:
  for a, n in X: print(a)
  exit()

# s * A^x <= t を満たす最大のxを返す
def flog(s, t, A):
  assert s<=t
  p = A
  for i in range(31):
    if s*p > t: return i
    p *= A

def compare(x1, x2):
  a1, n1 = x1
  a2, n2 = x2
  if n1-n2>40: return +1
  if n2-n1>40: return -1

  if n1==n2: return a1 - a2
  if n1>n2: return a1*A**(n1-n2) - a2
  if n2>n1: return a1 - a2*A**(n2-n1)

C = 0
L = 1
for i in range(1, N):
  ai, _ = X[i]
  c = 0
  Z = []
  for j in range(i):
    aj, nj = X[j]
    nj_ = flog(aj, ai, A)
    c += nj_ - nj
    Z.append((aj, nj_))

  if C+c <=B:
    C += c
    X[:i] = sorted(Z, key=cmp_to_key(compare))
    L = i+1
  else:
    break

R = B-C
Z = []
for i, (a, n) in enumerate(X[:L]):
  n_ = n + R//L
  if i < R%L: n_ += 1
  Z.append((a, n_))

X[:L] = Z
X = sorted(X, key=cmp_to_key(compare))

mod = 10**9+7
for a, n in X:
  print(a*pow(A, n, mod) % mod)
