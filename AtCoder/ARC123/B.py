N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

X = []
i = 0
for a in A:
  while i<N and B[i]<=a: i+= 1
  if i<N:
    X.append(B[i])
    i += 1

Y = []
i = 0
for x in X:
  while i<N and C[i]<=x: i+= 1
  if i<N:
    Y.append(C[i])
    i += 1

print(len(Y))
