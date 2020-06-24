N, S = input(), input()

clusters=[]
W, B = 0, 1
c_prev = None
seq=0
for c in S:
    if c != c_prev and c_prev!=None:
        clusters.append(seq)
        seq=0
    seq+=1
    c_prev=c
    
clusters.append(seq)
    
if S[0]=='.':
    clusters = [0] + clusters
if S[-1]=='#':
    clusters.append(0)

print(clusters)

min_nflip = nflip = sum(clusters[1::2])
for i in range(len(clusters)//2):
    nflip+=clusters[i*2]-clusters[i*2+1]
    min_nflip = min(min_nflip, nflip)

print(min_nflip)
