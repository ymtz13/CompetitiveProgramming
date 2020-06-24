N = int(input())
A = [int(c) for c in input().split()]

X = [None]*N
X[0] = sum(A) - sum(A[1::2])*2

for i in range(N-1):
    X[i+1] = 2*A[i]-X[i]

print(' '.join([str(x) for x in X]))
