import numpy as np
def test(N, A, B):
    ans = 0
    for X in range(N-A+1):
        for Y in range(N-A+1):
            M = np.zeros((N, N), bool)
            M[X:X+A, Y:Y+A] = True

            for x in range(N-B+1):
                for y in range(N-B+1):
                    if not np.any(M[x:x+B, y:y+B]): ans += 1
    return ans


T = int(input())
mod = 10**9+7

for _ in range(T):
    N, A, B = map(int, input().split())
    if A+B>N:
        print(0)
        continue
    
    X = N-A-B+1
    Z = X*(X+1)
    ans = Z*(2*(N-A+1)*(N-B+1)-Z)
    ans = 0 if ans<0 else ans%mod
    #print(ans, test(N,A,B))
    print(ans)
    
