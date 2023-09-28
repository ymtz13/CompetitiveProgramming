S = input()

ans = 0
for l in range(len(S)):
  for r in range(l, len(S)):
    s = S[l:r + 1]

    if s == s[::-1]:
      ans = max(ans, len(s))

print(ans)
