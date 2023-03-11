from collections import deque

N, K = map(int, input().split())
S = input()


def solve(N, K, S):
  queue = deque()
  queueY = deque()
  cntX = 0
  retval = 0

  for i, c in enumerate(S):
    queue.append((i, c))
    if c == 'Y': queueY.append(i)

    if c == 'X':
      cntX += 1
      if cntX > K:
        while queue and queue[0][1] == 'Y':
          queue.popleft()
          queueY.popleft()
        if queue:
          queue.popleft()
          cntX -= 1

    if not queue: continue

    L = queue[0][0]
    R = i

    outer = N - (R - L + 1)

    KK = K - cntX - outer

    if KK > 0:
      iY = queueY[KK - 1]
      L = iY + 1

    print(S, i, c, (cntX, outer, KK), [L, R], queue)

    retval = max(retval, R - L)

  return retval


ansL = solve(N, K, S)
ansR = solve(N, K, S[::-1])

print(max(ansL, ansR))
