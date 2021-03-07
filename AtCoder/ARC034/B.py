N = int(input())
ans = []
for f in range(200, 0, -1):
    x = N - f
    g = 0
    while x>0:
        g += x%10
        x //=10
    if f==g: ans.append(N-f)

print(len(ans))
if ans: print('\n'.join(map(str, ans)))
        
