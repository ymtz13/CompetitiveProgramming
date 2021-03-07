N = int(input())
XYC = [tuple(map(int, input().split())) for _ in range(N)]

def check(t):
    xmin = ymin = -1000000
    xmax = ymax = +1000000

    for x, y, c in XYC:
        d = t/c
        xmin = max(xmin, x-d)
        xmax = min(xmax, x+d)
        ymin = max(ymin, y-d)
        ymax = min(ymax, y+d)
    
    return xmin<=xmax and ymin<=ymax

min_ok = 10**10
max_ng = -1

while min_ok-max_ng>0.00001:
    tgt = (min_ok+max_ng)/2
    if check(tgt):
        min_ok = tgt
    else:
        max_ng = tgt

print(min_ok)