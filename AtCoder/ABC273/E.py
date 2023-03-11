from collections import defaultdict

Q = int(input())

P = [None]
V = [-1]
ans = []

Note = defaultdict(int)
i = 0

for _ in range(Q):
  query = tuple(input().split())

  if len(query) == 1:
    command = 'DELETE'
  else:
    command, arg = query
    arg = int(arg)

  if command == 'ADD':
    P.append(i)
    V.append(arg)
    i = len(P) - 1
    ans.append(arg)

  if command == 'DELETE':
    if i > 0: i = P[i]
    ans.append(V[i])

  if command == 'SAVE':
    Note[arg] = i
    ans.append(V[i])

  if command == 'LOAD':
    i = Note[arg]
    ans.append(V[i])

print(' '.join(map(str, ans)))
