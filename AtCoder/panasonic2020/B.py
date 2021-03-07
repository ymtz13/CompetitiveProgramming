H, W = map(int, input().split())
if H==1 or W==1:
  print(1)
  exit()
Wo = (W+1)//2
We = W//2
Ho = (H+1)//2
He = H//2
print(Wo*Ho + We*He)
