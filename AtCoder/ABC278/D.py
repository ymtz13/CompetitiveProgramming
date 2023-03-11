N = int(input())
A = list(map(int, input().split()))
B = [-1] * N
G = -2

ans = []
Q = int(input())
for q in range(Q):
  query = tuple(map(int, input().split()))

  if query[0] == 1:
    x = query[1]
    V = x
    G = q

  if query[0] == 2:
    i, x = query[1:]
    i -= 1

    if B[i] < G: A[i] = V

    A[i] += x
    B[i] = q

  if query[0] == 3:
    i = query[1]
    i -= 1

    if B[i] < G: A[i] = V

    ans.append(A[i])

for a in ans:
  print(a)
