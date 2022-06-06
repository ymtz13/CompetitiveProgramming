N = int(input())
U = [False] * (2 * N + 1)

for _ in range(N + 1):
  for i, u in enumerate(U):
    if not u:
      print(i + 1)
      U[i] = True
      break

  U[int(input()) - 1] = True
