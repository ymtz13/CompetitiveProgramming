N = 13
S = [
    'abcdefghijkll',
    'oqsuwynprtvxz',
    'cfilbehkadgjj',
    'quyptxoswnrvz',
    'ejbgldiafkchh',
    'syrxqwpvountz',
    'gahbicjdkelff',
    'upxsnvqytowrz',
    'ieajfbkgclhdd',
    'wtqnxuroyvspz',
    'kigecaljhfdbb',
    'yxwvutsrqponz',
    'qtwmkmsmomamn',
]

print(N)
print('\n'.join(S))

V = set()
m = 0
for i in range(13):
    for j in range(12):
        sp = S[i][j]
        for p in range(j+1, 13):
            sp = sp + S[i][p]
            if sp in V: print(i,j,sp)
            V.add(sp)
            m+= 1
                        
for j in range(13):
    for i in range(12):
        sq = S[i][j]
        for q in range(i+1, 13):
            sq = sq + S[q][j]
            if sq in V: print(i,j,sq)
            V.add(sq)
            m+=1

print(N*N*(N-1), len(V), m)
        
