N = int(input())
A = list(map(int, input().split()))

if N%2==0:
    S = [0]*N
    s = 0
    for i in range(0, N, 2):
        s += A[i]
        S[i] = s

    ans = s = sum(A[1:N:2])
    for t in range(1, N, 2):
        s -= A[t]
        ans = max(ans, S[t-1]+s)
    print(ans)

else:
    S = [0]*N
    s = 0
    p = 0
    for t in range(2, N, 2):
        p += A[t-2]
        S[t] = max(S[t-2]+A[t-1], p)
    
    ans = s = sum(A[2:N:2])
    for t in range(2, N, 2):
        s -= A[t]
        ans = max(ans, S[t]+s)
    print(ans)
    
