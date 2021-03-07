X, Y, A, B = map(int, input().split())
ans = 0
while X*(A-1)<B and X*A<Y:
    ans += 1
    X *= A

ans += (Y-1-X)//B
print(ans)
