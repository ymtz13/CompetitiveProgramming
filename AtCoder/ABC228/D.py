N = 1 << 20
A = [-1] * N
P = list(range(N))

Q = int(input())
for _ in range(Q):
  t, x = map(int, input().split())

  if t == 1:
    h = x % N
    H = [h]
    while A[h] != -1:
      h = P[h]
      H.append(h)

    A[h] = x

    g = (h + 1) % N
    for h in H:
      P[h] = g

  if t == 2:
    print(A[x % N])
