N = int(input())
H = list(map(int, input().split()))
ans = 0
for l in range(1, max(H)+1):
    streak = False
    for h in H:
        if h>=l:
            streak=True
        elif streak:
            streak=False
            ans+=1
    if streak: ans+=1

print(ans)
        
        
