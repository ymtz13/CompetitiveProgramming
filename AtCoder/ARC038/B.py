H, W = map(int, input().split())
S = [input() + '#' for _ in range(H)] + ['#'*(W+1)]
X = [[None]*W for _ in range(H)]

for h in range(H-1, -1, -1):
  for w in range(W-1, -1, -1):
    r = S[h  ][w+1]=='#' or X[h  ][w+1]
    b = S[h+1][w  ]=='#' or X[h+1][w  ]
    d = S[h+1][w+1]=='#' or X[h+1][w+1]
    X[h][w] = not r or not b or not d

print('First' if X[0][0] else 'Second')