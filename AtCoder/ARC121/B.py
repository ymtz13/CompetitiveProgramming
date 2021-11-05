N = int(input())
A = [input().split() for _ in range(N*2)]
R = [(int(a), c) for a, c in A if c=='R']
G = [(int(a), c) for a, c in A if c=='G']
B = [(int(a), c) for a, c in A if c=='B']

pR = len(R)%2
pG = len(G)%2
pB = len(B)%2

if pR==0 and pG==0 and pB==0:
  print(0)
  exit()

if pG==0: R, G = G, R
if pB==0: R, B = B, R


dRG = dRB = dGB = INF = 10**20
RG = sorted(R+G)
RB = sorted(R+B)
GB = sorted(B+G)

pa = pc = None
for a, c in RG:
  if pc and pc!=c: dRG = min(dRG, a - pa)
  pa = a
  pc = c

pa = pc = None
for a, c in RB:
  if pc and pc!=c: dRB = min(dRB, a - pa)
  pa = a
  pc = c

pa = pc = None
for a, c in GB:
  if pc and pc!=c: dGB = min(dGB, a - pa)
  pa = a
  pc = c

#print(RG, RB, GB)
#print(dRG, dRB, dGB)

print(min(dRG+dRB, dGB))
