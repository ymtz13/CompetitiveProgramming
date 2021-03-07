H, W = map(int, input().split())
C_ = [list(map(int, input().split())) for _ in range(H)]
C = []
for c in C_: C += c

def dfs(B, C, n, h, w, dh, dw):
  i = h*W + w
  j = i + dw + dh*W
  C[i] = C[j]
  C[j] = 0

  B[n].append(tuple(C))
  if n<12:
    hn = h + dh
    wn = w + dw
    if dh!=+1 and hn>0  : dfs(B, C, n+1, hn, wn, -1,  0)
    if dh!=-1 and hn<H-1: dfs(B, C, n+1, hn, wn, +1,  0)
    if dw!=+1 and wn>0  : dfs(B, C, n+1, hn, wn,  0, -1)
    if dw!=-1 and wn<W-1: dfs(B, C, n+1, hn, wn,  0, +1)
  
  C[j] = C[i]
  C[i] = 0

B = [[] for _ in range(13)]
i0 = C.index(0)
dfs(B, C, 0, i0//W, i0%W, 0, 0)

C2 = [(x+1)%(H*W) for x in range(H*W)]
B2 = [[] for _ in range(13)]
dfs(B2, C2, 0, H-1, W-1, 0, 0)

g = B2[0][0]

for n, b in enumerate(B):
  if g in b:
    print(n)
    exit()

b12 = sorted(B[12])
for n, b in enumerate(B2):
  b = sorted(b)
  l = len(b)
  i = 0
  for c in b12:
    while i+1<l and b[i]<c: i+=1
    if b[i]==c:
      print(12+n)
      exit()

print(24)
