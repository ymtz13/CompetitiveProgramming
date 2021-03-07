K = int(input())
L = [False]*K
X = 7
ans = 0
R = 0
while not L[0]:
    ans += 1
    X %= K
    R = (R+X)%K
    X *= 10
    if L[R]:
        ans = -1
        break
    L[R] = True
    

print(ans)
