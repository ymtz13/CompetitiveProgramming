X = list(map(int, input()))
ans = 'Strong'
if len(set(X)) == 1: ans = 'Weak'

if len([i for i in range(3) if X[i + 1] == (X[i] + 1) % 10]) == 3:
  ans = 'Weak'

print(ans)
