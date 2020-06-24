N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
IAB = [(i, A[i], B[i]) for i in range(N)]

ans = 10**9
pos_0 = 0b101010101010101010
for color in range(2**N):
    C = [b if (color>>i)&1 else a for i,a,b in IAB]
    pos_1 = color ^ pos_0
    P = [(pos_1>>i)&1 for i in range(N)]

    C_sorted = sorted(C)

    n_operation = 0
    for i in range(N):
        found = False
        for j in range(i, N):
            if C[j]==C_sorted[i] and P[j]==i&1:
                found = True
                break

        if found:
            n_operation += j-i
            for j in range(j, i, -1):
                C[j], C[j-1] = C[j-1], C[j]
                P[j], P[j-1] = P[j-1], P[j]
        else:
            break
                
    if found:
        ans = min(ans, n_operation)
    
print(ans if ans < 10**9 else -1)
