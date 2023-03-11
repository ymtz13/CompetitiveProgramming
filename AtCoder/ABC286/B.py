N = int(input())
S = input() + '_'
ans = []

i = 0
while i < N:
  if S[i:i + 2] == 'na':
    ans.append('nya')
    i += 2
  else:
    ans.append(S[i])
    i += 1

print(''.join(ans))
