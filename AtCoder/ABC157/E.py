N = int(input())
S = input()

L = 20
M = [1<<i for i in range(L)]
T = [[0]*m for m in M]

o = ord('a')

for i, c in enumerate(S):
    T[-1][i] = 1<<(ord(c)-o)

for l in range(L-2, -1, -1):
    for i in range(M[l]):
        T[l][i] = T[l+1][i*2] | T[l+1][i*2+1]
    
def q(layer, n, l, r):
    length_block = (1<<(L-1))//M[layer]
    ml = length_block*n
    mr = ml + length_block

    if l==ml and r==mr:
        return T[layer][n]
    
    center = ml + length_block//2

    ret = 0
    if l<center: ret |= q(layer+1, n*2  , l, min(r,center))
    if r>center: ret |= q(layer+1, n*2+1, max(l,center), r)

    return ret

Q = int(input())
for _ in range(Q):
    t, a1, a2 = input().split()
    if t=='1':
        i = int(a1)-1
        c = a2
        T[-1][i] = 1<<(ord(c)-o)
        for l in range(L-2, -1, -1):
            i = i//2
            T[l][i] = T[l+1][i*2] | T[l+1][i*2+1]
        
    else:
        l = int(a1)-1
        r = int(a2)
        x = q(0, 0, l, r)
        ans = 0
        for i in range(26):
            if (x>>i)&1: ans+=1
        print(ans)
        
