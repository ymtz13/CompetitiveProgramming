N = int(input())
S = input()
ans = []

X = 0
for c in S:
  if c == 'A':
    X += 2
  if c == 'B':
    X += 1
  if c == 'C':
    ans.extend(['A' * (X // 2), 'B' * (X % 2), 'C'])
    X = 0

ans.extend(['A' * (X // 2), 'B' * (X % 2)])

print(''.join(ans))
