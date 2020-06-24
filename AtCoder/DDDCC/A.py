X, Y = list(map(int, input().split()))
p = [0, 300000, 200000, 100000] + [0]*1000
ans = p[X]+p[Y]
if X==1 and Y==1 : ans+=400000
print(ans)
