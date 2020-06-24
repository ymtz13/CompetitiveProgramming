N = int(input())
A = list(map(int, input().split()))
B = [None]*N

for n in range(N, 0, -1):
    B[n-1] = A[n-1]
    k=n*2
    while k<=N:
        B[n-1] ^= B[k-1]
        k += n

M = sum(B)
print(M)
if M>0:
    print(' '.join( [str(i+1) for i,b in enumerate(B) if b==1] ))
