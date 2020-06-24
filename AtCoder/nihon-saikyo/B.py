N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
S = [0]*N
T = [0]*N
for i, a in enumerate(A):
    for j, a_ in enumerate(A):
        if a_<a: S[i]+=1
        if j>i and a_<a: T[i]+=1

print((K*(K-1)//2*sum(S) + sum(T)*K)%(10**9+7))

