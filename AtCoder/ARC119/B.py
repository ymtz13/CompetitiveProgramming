N = int(input())
S = input()
T = input()

M = S.count('0')
if M != T.count('0'):
  print(-1)
  exit()

From = [i for i, c in enumerate(S) if c=='0']
To   = [i for i, c in enumerate(T) if c=='0']

ans = 0
for f, t in zip(From, To):
  if f!=t: ans += 1

print(ans)
