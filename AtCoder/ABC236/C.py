N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

t = set(T)
for s in S:
  print('Yes' if s in t else 'No')
