A, B, K = map(int, input().split())
for k in range(K):
  if k%2==0:
    A -= A % 2
    A //= 2
    B += A
  else:
    B -= B % 2
    B //= 2
    A += B

print(A, B)