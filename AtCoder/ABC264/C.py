H1, W1 = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H1)]

H2, W2 = map(int, input().split())
B = [tuple(map(int, input().split())) for _ in range(H2)]

IH = []
for bH in range(1 << H1):
  iH = [i for i in range(H1) if (bH >> i) & 1]
  if len(iH) != H2: continue
  IH.append(iH)

IW = []
for bW in range(1 << W1):
  iW = [i for i in range(W1) if (bW >> i) & 1]
  if len(iW) != W2: continue
  IW.append(iW)

for iH in IH:
  for iW in IW:
    ans = True
    for h, ih in enumerate(iH):
      for w, iw in enumerate(iW):
        if A[ih][iw] != B[h][w]:
          ans = False
          break
      if not ans: break

    if ans:
      print('Yes')
      exit()

print('No')
