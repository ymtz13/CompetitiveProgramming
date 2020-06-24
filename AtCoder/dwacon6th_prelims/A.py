N = int(input())
ST = []
for _ in range(N):
    s, t = input().split()
    ST.append((s, int(t)))
X = input()
ans = 0
sleep = False
for s, t in ST:
    if sleep: ans+=t
    if s==X: sleep=True
print(ans)
    
