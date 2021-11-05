K = int(input())
A, B = input().split()


def conv(X):
  v = 0
  d = 1
  for c in X[::-1]:
    v += d * int(c)
    d *= K
  return v


print(conv(A) * conv(B))
