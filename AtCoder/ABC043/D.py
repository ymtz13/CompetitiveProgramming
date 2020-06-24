s = input()
for x in list(map(chr, range(ord('a'), ord('z')+1))):
    p = None
    for i, c in enumerate(s):
        if c!=x: continue
        if p is not None and i-p<=2:
            print(p+1, i+1)
            exit()
        p = i

print(-1, -1)
