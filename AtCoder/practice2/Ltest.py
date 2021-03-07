N, Q = map(int, input().split())
A = list(map(int, input().split()))

def flip(L, R):
    for i in range(L-1, R): A[i] = 1-A[i]

def query(L,R):
    n1 = retval = 0
    for i in range(L-1, R):
        if A[i]==1: n1+=1
        else: retval += n1
    return retval

for q in range(Q):
    T, L, R = map(int, input().split())
    if T==1: flip(L,R)
    else: print(q, query(L,R),'query({:2d}, {:2d})'.format(L, R), A)
