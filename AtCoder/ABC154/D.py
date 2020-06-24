N, K = map(int, input().split())
P = list(map(int, input().split()))
Q = [(p+1)/2 for p in P]
ans = s = sum(Q[:K])
for i in range(K, N):
    s += Q[i] - Q[i-K]
    ans = max(ans, s)
print(ans)
    
