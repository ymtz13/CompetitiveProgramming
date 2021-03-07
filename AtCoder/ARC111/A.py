N, M = map(int, input().split())

if M==1:
  print(0)
  exit()

R = 1
S = 0
D = [set() for _ in range(10000)]
A = []
while S not in D[R]:
  A.append(10000*R+S)
  D[R].add(S)
  R10 = 10*R
  R = R10 % M
  S = (10*S + R10//M) % M

O = A.index(10000*R+S)
P = len(A) - O
I = (N-O)%P+O if N>=O else N
print(A[I]%10000)
