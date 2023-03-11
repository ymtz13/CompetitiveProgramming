X = sorted(list(map(int, input().split())))
S = set(X)
if len(S) != 2:
  print('No')
  exit()

P, Q = tuple(S)
print('Yes' if {X.count(P), X.count(Q)} == {2, 3} else 'No')
