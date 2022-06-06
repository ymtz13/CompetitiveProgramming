from collections import deque

N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

N2 = N * N
M = [0] * N2
D = [0] * N2

for x in range(N):
  S = input()
  for i, c in enumerate(S, x * N):
    if c == '#': M[i] = 4


def printM(M):
  for x in range(N):
    print(M[x * N:x * N + N])


queue = [(Ax - 1) * N + Ay - 1]
d = 1
while queue:
  queue_next = []

  for q in queue:
    if D[q] == 0: D[q] = d

    # LU
    for t in range(q - N - 1, -1, -N - 1):
      if t % N == N - 1: break
      if D[t] != 0 or (M[t] & 0b101): break
      queue_next.append(t)
      M[t] |= 0b001

    # RD
    for t in range(q + N + 1, N2, +N + 1):
      if t % N == 0: break
      if D[t] != 0 or (M[t] & 0b101): break
      queue_next.append(t)
      M[t] |= 0b001

    # LD
    for t in range(q + N - 1, N2, +N - 1):
      if t % N == N - 1: break
      if D[t] != 0 or (M[t] & 0b110): break
      queue_next.append(t)
      M[t] |= 0b010

    # RU
    for t in range(q - N + 1, -1, -N + 1):
      if t % N == 0: break
      if D[t] != 0 or (M[t] & 0b110): break
      queue_next.append(t)
      M[t] |= 0b010

  queue = queue_next
  d += 1

#printM(D)

print(D[(Bx - 1) * N + By - 1] - 1)
