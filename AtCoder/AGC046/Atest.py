A, B, C, D = map(int, input().split())
nR = C-A
nC = D-B
L = [None]*nR

def dfs(i):
    if i<nR:
        retval = 0
        for x in range(D):
            L[i] = x
            retval += dfs(i+1)
        return retval

    
    retval = 1
    k = B-1
    for j, l in enumerate(L+[D-1]):
        knext = max(k, l)
        for s in range(k+1, knext+1):
            retval *= (A+j)
            print(retval, l)
        k = knext

    print(L, retval)

    return retval
        

print(dfs(0))
