S = input()
L = len(S)

ans = 0
for l in range(1, L):
  ans += pow(26, l)

for i, c in enumerate(S, 1):
  x = ord(c) - ord('A')
  ans += pow(26, L - i) * x

print(ans + 1)
