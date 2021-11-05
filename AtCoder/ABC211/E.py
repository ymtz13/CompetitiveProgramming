N = int(input())
K = int(input())
S = [[2] * (N + 2) for _ in range(N + 2)]
B = [[0] * (N + 2) for _ in range(N + 2)]

x = 0
for h in range(1, N + 1):
  for w, c in enumerate(input(), 1):
    S[h][w] = 2 if c == '#' else 0
    B[h][w] = 1 << ((h - 1) * N + w - 1)
    x += S[h][w] * B[h][w]

X = set()
ans = 0


def dfs(i, x):
  global ans
  global X

  if x in X: return
  X.add(x)

  if i == K:
    ans += 1
    return

  for h in range(1, N + 1):
    for w in range(1, N + 1):

      if S[h][w] == 0 and (i == 0 or S[h][w + 1] == 1 or S[h][w - 1] == 1
                           or S[h + 1][w] == 1 or S[h - 1][w] == 1):
        S[h][w] = 1
        x += B[h][w]

        dfs(i + 1, x)

        S[h][w] = 0
        x -= B[h][w]


dfs(0, x)

print(ans)
