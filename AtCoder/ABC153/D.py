H = int(input())
ans = 0
n = 1
while H:
    ans+=n
    H//=2
    n*=2
print(ans)
    
