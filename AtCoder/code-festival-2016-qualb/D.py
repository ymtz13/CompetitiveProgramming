N = int(input())
ans = int(input())-1
x = 1
for i in range(N-1):
    A = int(input())
    if A>x+1: ans += (A-1)//(x+1)
    elif A==x+1: x=A

print(ans
    
