N, M = list(map(int, input().split()))
wa = [0]*N
solved = [False]*N
for _ in range(M):
    p, S = input().split()
    p = int(p)-1
    if S=='WA' and not solved[p]:
        wa[p]+=1
    if S=='AC':
        solved[p] = True

ans1 = 0
ans2 = 0
for w, s in zip(wa, solved):
    if s:
        ans1 += 1
        ans2 += w

print(ans1, ans2)
    
        
    
