N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A = sorted(A)
B = sorted(B)

K = N//2
if N%2==0:
    a = A[K-1]+A[K]
    b = B[K-1]+B[K]
    print(b-a+1)
    
else:
    print(B[K]-A[K]+1)
