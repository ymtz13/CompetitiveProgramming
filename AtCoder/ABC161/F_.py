N = int(input())
for K in range(2,N):
    while N%K==0: N//=K
    if N%K==1: print(K)
