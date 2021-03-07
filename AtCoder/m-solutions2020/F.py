N = int(input())
PU = []
PR = []
PD = []
PL = []
P = {'U':PU, 'R':PR, 'D':PD, 'L':PL}
for _ in range(N):
    X, Y, U = input().split()
    P[U].append((int(X), int(Y)))

ans = 100000000
    
# ===== 1 =====
DU = {}
for x, y in PU:
    if x not in DU: DU[x] = []
    DU[x].append(y)

DD = {}
for x, y in PD:
    if x not in DD: DD[x] = []
    DD[x].append(y)

for x, p1 in DU.items():
    if x not in DD: continue
    p2 = DD[x]
    
    p1.sort()
    p2.sort()
    n = len(p2)
    i = 0
    for z in p1:
        while i<n and p2[i]<=z: i+=1
        if i==n: break
        ans = min(ans, (p2[i]-z)*5)

# ===== 2 =====
DR = {}
for x, y in PR:
    if y not in DR: DR[y] = []
    DR[y].append(x)

DL = {}
for x, y in PL:
    if y not in DL: DL[y] = []
    DL[y].append(x)

for y, p1 in DR.items():
    if y not in DL: continue
    p2 = DL[y]

    p1.sort()
    p2.sort()
    n = len(p2)
    i = 0
    for z in p1:
        while i<n and p2[i]<=z: i+=1
        if i==n: break
        ans = min(ans, (p2[i]-z)*5)

# ===== 3-1 =====
DR = {}
for x, y in PR:
    if x+y not in DR: DR[x+y] = []
    DR[x+y].append(x)

DU = {}
for x, y in PU:
    if x+y not in DU: DU[x+y] = []
    DU[x+y].append(x)

for key, p1 in DR.items():
    if key not in DU: continue
    p2 = DU[key]

    p1.sort()
    p2.sort()
    n = len(p2)
    i = 0
    for z in p1:
        while i<n and p2[i]<=z: i+=1
        if i==n: break
        ans = min(ans, (p2[i]-z)*10)

# ===== 3-2 =====
DD = {}
for x, y in PD:
    if x+y not in DD: DD[x+y] = []
    DD[x+y].append(x)

DL = {}
for x, y in PL:
    if x+y not in DL: DL[x+y] = []
    DL[x+y].append(x)

for key, p1 in DD.items():
    if key not in DL: continue
    p2 = DL[key]

    p1.sort()
    p2.sort()
    n = len(p2)
    i = 0
    for z in p1:
        while i<n and p2[i]<=z: i+=1
        if i==n: break
        ans = min(ans, (p2[i]-z)*10)

# ===== 4-1 =====
DR = {}
for x, y in PR:
    if x-y not in DR: DR[x-y] = []
    DR[x-y].append(x)

DD = {}
for x, y in PD:
    if x-y not in DD: DD[x-y] = []
    DD[x-y].append(x)

for key, p1 in DR.items():
    if key not in DD: continue
    p2 = DD[key]

    p1.sort()
    p2.sort()
    n = len(p2)
    i = 0
    for z in p1:
        while i<n and p2[i]<=z: i+=1
        if i==n: break
        ans = min(ans, (p2[i]-z)*10)

# ===== 4-2 =====
DU = {}
for x, y in PU:
    if x-y not in DU: DU[x-y] = []
    DU[x-y].append(x)

DL = {}
for x, y in PL:
    if x-y not in DL: DL[x-y] = []
    DL[x-y].append(x)

for key, p1 in DU.items():
    if key not in DL: continue
    p2 = DL[key]

    p1.sort()
    p2.sort()
    n = len(p2)
    i = 0
    for z in p1:
        while i<n and p2[i]<=z: i+=1
        if i==n: break
        ans = min(ans, (p2[i]-z)*10)
        
# ===== ans =====
print(ans if ans<100000000 else 'SAFE')
