N, S = input().split()
nA = nT = nC = nG = 0
ans = 0
X = {(0,0): 1}

for c in S:
    if c=='A': nA+=1
    if c=='T': nT+=1
    if c=='C': nC+=1
    if c=='G': nG+=1

    dAT = nA - nT
    dCG = nC - nG
    k = (dAT, dCG)
    if k in X:
        ans += X[k]
        X[k] += 1
    else:
        X[k] = 1

print(ans)

    
    

    
