N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
s = 0
B = [0]
C = {0:[0]}
for i, a in enumerate(A):
    s = (s+a)%K
    n = (s-i-1)%K
    B.append(n)
    if n not in C: C[n] = []
    C[n].append(i+1)
    
print(B)
print(C)

ans = 0

for k, v in C.items():
    if len(v)<=1: continue
    ans_k = 0
    ir=0
    for il in range(0,len(v)-1):
        l = v[il]
        while(ir<len(v) and v[ir]-l<=K-1): ir+=1
        ans_k+=(ir-1)-il
    ans+=ans_k
print(ans)
