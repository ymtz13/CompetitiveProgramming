N, K, C = map(int, input().split())
S = input()

if N==1:
    print(1)
    exit()

Af = [0]*N
Rf = [0]*N
d = 0
f = 0
for i, s in enumerate(S):
    f-=1
    if s=='o' and f<0:
        d+=1
        f=C
    Af[i]=d
    Rf[i]=C-f

Ab = [0]*N
Rb = [0]*N
d = 0
f = 0
for i, s in enumerate(S[::-1]):
    f-=1
    if s=='o' and f<0:
        d+=1
        f=C
    Ab[N-i-1]=d
    Rb[N-i-1]=C-f

if Ab[1]<K:
    print(1)

for i in range(1, N-1):
    if Af[i-1]+Ab[i+1]>K: continue
    if Af[i-1]+Ab[i+1]==K and Rf[i-1]+Rb[i+1]+1>=C: continue
    print(i+1)

if Af[-2]<K:
    print(N)
