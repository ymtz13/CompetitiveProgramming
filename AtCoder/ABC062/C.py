H, W = list(map(int, input().split()))
ans = 10**10

for w1 in range(1, W//2+1):
    s1 = H*w1

    w2 = (W-w1)//2
    w3 = W-w1-w2
    s2 = H*w2
    s3 = H*w3
    ans = min(ans, max(s1, s2, s3)-min(s1,s2,s3))

    h2 = H//2
    h3 = H-h2
    s2 = (W-w1)*h2
    s3 = (W-w1)*h3
    ans = min(ans, max(s1, s2, s3)-min(s1,s2,s3))

H, W = W, H


for w1 in range(1, W//2+1):
    s1 = H*w1

    w2 = (W-w1)//2
    w3 = W-w1-w2
    s2 = H*w2
    s3 = H*w3

    ans = min(ans, max(s1, s2, s3)-min(s1,s2,s3))

    h2 = H//2
    h3 = H-h2
    s2 = (W-w1)*h2
    s3 = (W-w1)*h3
    ans = min(ans, max(s1, s2, s3)-min(s1,s2,s3))

print(ans)
