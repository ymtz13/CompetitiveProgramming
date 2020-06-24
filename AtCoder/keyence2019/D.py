N, M = list(map(int, input().split()))
A = sorted(list(map(int, input().split())), reverse=True)+[-1]
B = sorted(list(map(int, input().split())), reverse=True)+[-1]
nA = nB = 0
ans = 1
mod = 10**9+7
for x in range(N*M, 0, -1):
    r = 1
    if x==A[nA] and x==B[nB]:
        nA += 1
        nB += 1
    elif x==A[nA] and x!=B[nB]:
        nA += 1
        r = nB
    elif x!=A[nA] and x==B[nB]:
        nB += 1
        r = nA
    else:
        r = nA*nB - (N*M-x)
        
    ans = ans*r % mod
print(ans)

