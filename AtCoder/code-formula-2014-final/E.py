S = input()
# S = 'babaa'
# S = 'aababaabaababaabaababaababaabaabab'

if S == 'b':
  print(1, 0)
  exit()

Fib = [1, 1]
while Fib[-1] != len(S):
  Fib.append(sum(Fib[-2:]))

indent = 0
memo = {}


def solve(s, i):
  if i == 0: return [0] if s == 'b' else []
  if i == 1: return [0] if s == 'a' else []

  if s in memo: return memo[s]

  global indent
  indent += 1
  # print('  ' * indent, '+', s, i)

  f1 = Fib[i - 1]
  f2 = Fib[i - 2]

  V1 = solve(s[:f1], i - 1)
  V2 = solve(s[f1:], i - 2)
  # print('  ' * indent, ':', V1, V2)

  R = []
  for v1 in V1:
    for v2 in V2:
      if v1 // 2 == v2: R.append(v1 * 2)

  V1 = solve(s[f2:], i - 1)
  V2 = solve(s[:f2], i - 2)
  # print('  ' * indent, ':', V1, V2)

  for v1 in V1:
    for v2 in V2:
      if v1 // 2 == v2: R.append(v1 * 2 + 1)

  # print('  ' * indent, '-', s, i, R)
  indent -= 1

  memo[s] = R

  return R


ans = solve(S, len(Fib) - 1)
print(len(Fib), ans[0])
