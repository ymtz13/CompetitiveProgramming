A = input()
N = len(A)
d = 0
for i in range(N//2):
  if A[i] != A[N-1-i]: d += 1

if d==0:
  x = 25 * (N%2)
elif d==1:
  x = 2
else:
  x = 0

print(25*N-x)