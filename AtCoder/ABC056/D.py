import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
modmask = 2**K - 1

# K-a <= x <= K-1

dp_L = [1] * N
p = 1
for i, a in enumerate(A[:-1]):
    if a<K: p = (p|(p<<a)) & modmask
    dp_L[i+1] = p

dp_R = [1] * N
p = 1
for i, a in enumerate(reversed(A[1:])):
    if a<K : p = (p|(p<<a)) & modmask
    dp_R[i+1] = p
    
#for i, d in enumerate(dp_L):
#    print('{:2d} {:20b}'.format(i, d))

#for i, d in enumerate(dp_R):
#    print('{:2d} {:20b}'.format(i, d))

ans = 0
for i, a in enumerate(A):
    dl = dp_L[i]
    dr = dp_R[-(i+1)]
    #print(i, '{:20b} {:20b}'.format(dl, dr))
    Fl = []
    
    noneed = True
    ml = -K
    for j in range(K):
        #fl = dl&(1<<j)
        fl = dl&1
        dl>>=1
        fr = dr&(1<<(K-1-j))
        if fl: ml = j
        if fr and j-ml<a:
            #print(j, ml, K-1-j)
            noneed = False
            break
    #print('noneed:', noneed,'\n')
    if noneed: ans+=1

print(ans)
