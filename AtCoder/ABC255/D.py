N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
S = sum(A)
X = sorted([(int(input()), q) for q in range(Q)])
ans = [None] * Q

i = 0
s = 0
for x, q in X:
  while i < N and A[i] < x:
    s += A[i]
    i += 1

  a1 = i * x - s
  a2 = S - s - (N - i) * x
  ans[q] = a1 + a2

for a in ans:
  print(a)
