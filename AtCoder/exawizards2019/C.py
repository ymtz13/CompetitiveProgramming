N, Q = map(int, input().split())
S = input()
P = [tuple(input().split()) for _ in range(Q)]

Sinv = S[::-1]
Pinv = [(t, 'L' if d == 'R' else 'R') for t, d in P]


def check(i, S, P):
  for t, d in P:
    if S[i] == t:
      i += 1 if d == 'R' else -1

    if i < 0: return True
    if i > N - 1: return False
  return False


def num_fall_left(S, P):
  ok = 0
  ng = N + 1

  while ng - ok > 1:
    tgt = (ok + ng) // 2
    if check(tgt - 1, S, P):
      ok = tgt
    else:
      ng = tgt

  return ok


ans = N - num_fall_left(S, P) - num_fall_left(Sinv, Pinv)
print(ans)
