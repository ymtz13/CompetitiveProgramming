from itertools import permutations

# N, K = map(int, input().split())


def valid(P, K):
  for i, v in enumerate(P, 1):
    if abs(i - v) < K:
      return False
  return True


def solve_bf(N, K):
  X = []

  for P in permutations(range(1, N + 1)):
    if not valid(P, K): continue
    # print(P)
    X.append(P)

  return list(min(X)) if X else -1


def solve(N, K):
  if K > N // 2:
    # print(-1)
    # exit()
    return -1

  ans = []
  for i in range(N // (2 * K)):
    s = i * (2 * K) + 1
    ans.extend(list(range(s + K, s + 2 * K)))
    ans.extend(list(range(s, s + K)))

  r = list(range(len(ans) + 1, N + 1))

  if len(r) <= K:
    ans = ans[:-K] + r + ans[-K:]
  else:
    t = len(r) % K
    ans = ans[:-(K - t)] + r[t:] + ans[-(K - t):] + r[:t]

  return ans


for N in range(1, 12):
  for K in range(1, N):
    ansbf = solve_bf(N, K)
    ans = solve(N, K)

    assert ansbf == ans, ((N, K), ansbf, ans)
    print(N, K, ansbf, ans)
