N = int(input())
D = set()
for d in range(N):
  S = input()
  if S not in D: print(d+1)
  D.add(S)
