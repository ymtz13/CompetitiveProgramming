N, K = list(map(int, input().split()))
H = [0]+list(map(int, input().split()))
C = [10**10] + [0]*N
for i in range(2,N+1):
    C[i] = min([C[i-j]+abs(H[i-j]-H[i]) for j in range(1,min(K+1, i))])
print(C[-1])
