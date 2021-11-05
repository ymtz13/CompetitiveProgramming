H, W = map(int, input().split())
if H==1 or W==1:
  print(H*W)
  exit()
h = (H+1)//2
w = (W+1)//2
print(h*w)
