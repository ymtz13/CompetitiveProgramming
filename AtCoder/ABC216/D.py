from collections import deque

N, M = map(int, input().split())
A = []
for _ in range(M):
  k = input()
  A.append(deque(map(int, input().split())))

#print(A)

queue = deque([(q.popleft(), i) for i, q in enumerate(A)])

#print(A)
#print(queue)

T = [None] * (N + 1)
cnt = 0
while queue:
  a, i = queue.popleft()

  if T[a] is None:
    T[a] = i

  else:
    j = T[a]
    T[a] = None
    cnt += 1

    if A[j]: queue.append((A[j].popleft(), j))
    if A[i]: queue.append((A[i].popleft(), i))

print('Yes ' if cnt == N else 'No')
