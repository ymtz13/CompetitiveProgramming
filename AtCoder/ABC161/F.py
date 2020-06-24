N = int(input())

ans = 2 # N and N-1
for K in range(2, N):
    if K*K>N: break
    n = N
    if n%K!=0: continu-e
    while n%K==0: n//=K
    if n%K==1: ans +=1

y = 0
N_ = N-1
for K in range(2, N):
    if K*K>=N_: break
    if N_%K==0: y +=2
if K*K==N_: y += 1

print(ans+y)
