N, T = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)

T %= S

for i, a in enumerate(A, 1):
  if T >= a: T -= a
  else:
    print(i, T)
    exit()
