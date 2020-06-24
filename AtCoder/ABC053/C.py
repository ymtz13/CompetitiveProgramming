x = int(input())
ans = x//11*2
if x%11>0: ans += 1
if x%11>6: ans += 1
print(ans)
