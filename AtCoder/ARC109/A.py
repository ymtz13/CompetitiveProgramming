a, b, x, y = map(int, input().split())
z = min(2*x, y)
ans = x 
if a<b: ans = (b-a)*z + x
if a>b: ans = (a-b-1)*z + x
print(ans)