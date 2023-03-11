N = int(input())
A = list(map(int, input().split()))
P = 0
B = []

for a in A:
  B.append(0)
  X = [b + a for b in B]
  B = [x for x in X if x < 4]
  P += len(X) - len(B)

print(P)
