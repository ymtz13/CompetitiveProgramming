H, W = map(int, input().split())
ans = 0

S = input()
for i in range(1, W):
    if S[i]=='.' and S[i-1]=='.': ans += 1

for h in range(H-1):
    So = S
    S = input()

    for i in range(1, W):
        if S[i]=='.' and S[i-1]=='.': ans += 1

    for i in range(W):
        if S[i]=='.' and So[i]=='.': ans += 1

print(ans)

    
    
