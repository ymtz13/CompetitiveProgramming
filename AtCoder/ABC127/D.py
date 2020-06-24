N, M = [int(c) for c in input().split()]

A = sorted([int(c) for c in input().split()])

t = {}
for a in A:
    t[a] = t[a]+1 if a in t else 1

for i in range(M):
    B, C = [int(c) for c in input().split()]
    t[C] = t[C]+B if C in t else B

s,v=0,0
for k in sorted(t.keys(), reverse=True):
    v += k*min(N-s, t[k])
    s += t[k]
    if s>=N: break
    
print(v)
