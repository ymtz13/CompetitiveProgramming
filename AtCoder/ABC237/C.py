S = input()


def solve(S):
  if S.count('a') == len(S):
    return 'Yes'

  x = None
  for i, c in enumerate(S):
    if c != 'a':
      if x is None: x = i
      y = i

  z = len(S) - 1 - y

  if x > z: return 'No'

  T = 'a' * (z - x) + S

  return 'Yes' if T[::-1] == T else 'No'


print(solve(S))
