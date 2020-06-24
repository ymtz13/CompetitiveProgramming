S = [input() for _ in range(3)]
D = {'a':0, 'b':1, 'c':2}
N = [0]*3
p = 0
while N[p]<len(S[p]):
    p_new = D[S[p][N[p]]]
    N[p]+=1
    p = p_new

print('A' if p==0 else 'B' if p==1 else 'C')

