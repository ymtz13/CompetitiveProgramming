ans = 2000
H = int(input())
W = int(input())
N = int(input())
for nh in range(H+1):
    for nw in range(W+1):
        white = (H-nh)*(W-nw)
        if H*W-white>=N:
            ans = min(ans, nh+nw)
print(ans)
