N, X = map(int, input().split())
S = input()
for c in S:
  X = X + 1 if c=='o' else max(0, X-1)
print(X)
