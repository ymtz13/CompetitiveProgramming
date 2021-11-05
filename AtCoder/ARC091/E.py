from collections import deque

N, A, B = map(int, input().split())

if A + B > N + 1 or A * B < N:
  print(-1)
  exit()

X = A - ((N + B - 1) // B)

ans = list(range(B - 1, -1, -1))
for P in range(B, N, B):
  C = deque([P])
  for Q in range(P + 1, min(P + B, N)):
    if X > 0:
      C.append(Q)
      X -= 1
    else:
      C.appendleft(Q)

  ans.extend(list(C))

print(' '.join([str(i + 1) for i in ans]))
