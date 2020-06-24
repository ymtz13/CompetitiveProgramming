D, G = map(int, input().split())
P = [0]*D
C = [0]*D
for d in range(D):
    P[d], C[d] = map(int, input().split())

ans = 10000
for f in range(2**D):
    score_tot = 0
    q = 0
    for d in range(D):
        if f>>d&1:
            score_tot += C[d]+P[d]*(d+1)*100
            q += P[d]

    for d in range(D-1, -1, -1):
        if G <= score_tot: break
        if f>>d&1: continue
        score_d = (d+1)*100
        k = (G-score_tot-1)//score_d+1
        score_tot += min(k, P[d]) * score_d
        q += min(k, P[d])

    ans = min(ans, q)

print(ans)

    
    
