from collections import deque

N = int(input())
A = deque(sorted(list(map(int, input().split()))))

ans = 0

while len(A) > 1:
  ans += 1
  Ai = A.pop()
  Aj = A[0]

  R = Ai % Aj
  if R > 0: A.appendleft(R)

print(ans)
