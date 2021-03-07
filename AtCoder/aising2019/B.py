N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
X = [0]*3
for p in P:
  if   p <= A: i = 0
  elif p <= B: i = 1
  else       : i = 2

print(min(X))
