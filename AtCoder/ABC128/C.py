N, M = [int(c) for c in input().split()]

s = []
for i in range(M):
    s.append([int(c) for c in input().split()][1:])

p = [int(c) for c in input().split()]

sw = [0]*N
n = [0]

def f(i):
    if i==N:
        n[0]+=check()        
    else:
        sw[i]=0
        f(i+1)
        sw[i]=1
        f(i+1)

def check():
    all_light = True
    for s_m, p_m in zip(s,p):
        d=0
        for ss in s_m:
            d += sw[ss-1]
        if d%2 != p_m:
            all_light = False
            break
    return 1 if all_light else 0
            
f(0)

print(n[0])
