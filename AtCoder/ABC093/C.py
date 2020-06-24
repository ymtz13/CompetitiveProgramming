X = sorted(list(map(int, input().split())))
d1 = X[2]-X[0]
d2 = X[2]-X[1]

ans = d1//2 + d2//2
k = (d1&1) + (d2&1)
if k==2:
    ans += 1
elif k==1:
    ans += 2
print(ans)
