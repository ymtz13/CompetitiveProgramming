from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

queue = deque()
for i in range(N):
  if B[i] - B[(i - 1) % N] - B[(i + 1) % N] >= A[i]:
    queue.append(i)

ans = 0

while queue:
  ii = queue.popleft()
  l1 = (ii - 1) % N
  r1 = (ii + 1) % N
  l2 = (ii - 2) % N
  r2 = (ii + 2) % N

  Bl1 = B[l1]
  Bl2 = B[l2]
  Br1 = B[r1]
  Br2 = B[r2]

  D = Bl1 + Br1
  x = (B[ii] - A[ii]) // D
  ans += x
  B[ii] -= x * D

  B00 = B[ii]

  if B00 - Bl1 - Br1 >= A[ii]: queue.append(ii)
  if Bl1 - Bl2 - B00 >= A[l1]: queue.append(l1)
  if Br1 - Br2 - B00 >= A[r1]: queue.append(r1)

print(ans if A == B else -1)
