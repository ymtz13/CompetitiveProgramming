H, W = map(int, input().split())
S = [list(map(lambda c: 0 if c=='.' else 1, input())) for _ in range(H)]

ans = 0
for h in range(H-1):
  for w in range(W-1):
    X = 0
    X += S[h  ][w  ]
    X += S[h  ][w+1]
    X += S[h+1][w  ]
    X += S[h+1][w+1]
    if X == 1 or X == 3: ans += 1

print(ans)
