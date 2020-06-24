N, K = map(int, input().split())
A = list(map(int, input().split()))

x=1
while K:
    if K&1: x=A[x-1]
    K>>=1

    A2 = [None]*N
    for i,a in enumerate(A):
        A2[i]=A[A[i]-1]
    A=A2

print(x)
