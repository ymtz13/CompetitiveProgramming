N, M, T = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * N
for _ in range(M):
  X, Y = map(int, input().split())
  B[X - 1] = Y

for a, b in zip(A, B):
  T += b
  T -= a  
  if T <= 0:
    print('No')
    exit()

print('Yes')
