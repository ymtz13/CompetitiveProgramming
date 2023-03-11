from collections import deque

N = int(input())
X = list(map(int, input()))
X = [0] * (N - len(X)) + X

V = deque()
p = None
s = 0
for x in X:
  if x != p and p is not None:
    V.append((p, s))
    s = 0

  p = x
  s += 1

V.append((p, s))


def add1():
  x, n = V[-1]
  if x == 0:
    if n == 1:
      V.pop()
      _, n1 = V.pop() if len(V) else (1, 0)
      V.append((1, n1 + 1))

    else:
      V.pop()
      V.append((0, n - 1))
      V.append((1, 1))

  else:
    _, n1 = V.pop()
    add1()
    V.append((0, n1))


def sub1():
  x, n = V[-1]
  if x == 1:
    if n == 1:
      V.pop()
      _, n0 = V.pop() if len(V) else (0, 0)
      V.append((0, n0 + 1))

    else:
      V.pop()
      V.append((1, n - 1))
      V.append((0, 1))

  else:
    _, n0 = V.pop()
    sub1()
    V.append((1, n0))


def tostr():
  r = ''
  for x, n in V:
    r += str(x) * n
  return r


ans = [1]
for _ in range(N - 1):
  # print(ans, tostr(), int(tostr(), 2))

  sub1()
  if len(V) == 1 and V[0][0] == 0:
    break

  x, n = V.popleft()
  if n > 1: V.appendleft((x, n - 1))


  ans.append(x)
  if x == 1:
    add1()

print(''.join(map(str, ans)))
