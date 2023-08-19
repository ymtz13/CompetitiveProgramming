def solve(S, t, k):
  if t == 0:
    return S[k]

  w = 1 << t
  q = k // w
  r = k % w

  c = S[q]
  if c == 'A':
    return solve('BC', t - 1, r)
  if c == 'B':
    return solve('CA', t - 1, r)
  if c == 'C':
    return solve('AB', t - 1, r)


S = input()
Q = int(input())
ans = []

for _ in range(Q):
  t, k = map(int, input().split())
  if t > 72:
    t = 72 + t % 3

  ans.append(solve(S, t, k - 1))

for a in ans:
  print(a)
