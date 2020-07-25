N = int(input())
ans = [0]*(N+1)
for x in range(1,100):
    xx = x*x
    for y in range(1,100):
        yy = y*y
        xy = x*y
        for z in range(1,100):
            zz = z*z
            zx = z*x
            yz = y*z
            n = xx+yy+zz+xy+yz+zx
            if n<=N: ans[n]+=1

for n in range(1,N+1):
    print(ans[n])
