S = input() + '_'
T = input() + '_'

diff = 0
ok = False
for i in range(len(S) - 1):
  if S[i] != T[i]:
    diff += 1
    if S[i] == T[i + 1] and S[i + 1] == T[i]:
      ok = True

print('Yes' if diff == 0 or (diff == 2 and ok) else 'No')
