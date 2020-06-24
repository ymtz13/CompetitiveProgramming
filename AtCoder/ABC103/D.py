N, M = list(map(int, input().split()))
R = sorted([tuple(map(int, input().split())) for _ in range(M)])

ir = 0
d = N+1
ans = 0
for i in range(1, N):
    while ir<len(R) and R[ir][0]<=i:
        d = min(d, R[ir][1])
        ir+=1

    if d==i+1:
        d = N+1
        ans += 1

print(ans)
