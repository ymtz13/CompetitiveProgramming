N = input()[::-1]

dp1 = [0]
dp2 = [1]

for x in N:
    x = int(x)
    
    r = dp1[-1]+x
    if x<9: r = min(r, dp2[-1]+x+1)
    dp1.append(r)
    dp2.append(min(dp1[-2]+10-x, dp2[-1]+9-x))

print(dp1)
print(dp2)
    
print(min(dp1[-1],dp2[-1]+1))
