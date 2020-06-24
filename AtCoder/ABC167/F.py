N = int(input())
S = [input() for _ in range(N)]
B1 = []
B2 = []
for s in S:
    ncl = nop = 0
    for c in s:
        if c=='(':
            nop+=1
        else:
            if nop>0: nop-=1
            else: ncl+=1

    if nop-ncl>=0:
        B1.append((nop, ncl))
    else:
        B2.append((nop, ncl))

#print(B)
    
Bl = sorted(B1, key=lambda x:x[1])
Br = sorted(B2, key=lambda x:x[0])

xl = 0
for nop, ncl in Bl:
    if ncl>xl:
        print('No')
        exit()
    xl+=nop-ncl

xr = 0
for nop, ncl in Br:
    if nop>xr:
        print('No')
        exit()
    xr+=ncl-nop

print('Yes' if xl==xr else 'No')
