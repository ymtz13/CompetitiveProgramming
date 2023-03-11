from collections import deque

N = int(input())
A = list(map(int, input().split()))

S = set(A)
A = list(S) + [1 << 60] * (len(A) - len(S))
A = deque(sorted(A))

i = 0
while True:
  next = i + 1

  if len(A) == 0:
    print(i)
    exit()

  if len(A) == 1 and A[0] != next:
    print(i)
    exit()

  if A[0] == next:
    A.popleft()
  else:
    A.pop()
    A.pop()
  i = next
