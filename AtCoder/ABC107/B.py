H, W = map(int, input().split())
allwhite = [True]*W
M = []
for _ in range(H):
    s = input()
    if s.count('.')==W: continue
    M.append(s)
    for w,c in enumerate(s):
        allwhite[w] *= c=='.'
    

for s in M:
    for c,f in zip(s, allwhite):
        if not f: print(c, end='')
    print()
        
