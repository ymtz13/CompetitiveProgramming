def o(c):
  return ord(c) - ord('a')


N, K = map(int, input().split())
S = input()

D0 = [0] * 26
for c in S:
  D0[o(c)] += 1

D1 = D0[:]
ans = []

diff = 0
for i, c in enumerate(S):
  D0[o(c)] -= 1

  for x in range(26):
    if D1[x] == 0: continue
    if o(c) == x: break

    D1[x] -= 1
    d1 = len([None for c0, c1 in zip(S, ans + [x]) if c0 != c1])
    d2 = sum([max(0, x1 - x0) for x0, x1 in zip(D0, D1)])
    D1[x] += 1
    if d1 + d2 <= K: break

  D1[x] -= 1
  ans.append(chr(ord('a') + x))

print(''.join(ans))
