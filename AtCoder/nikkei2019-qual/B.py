N = input()
S = [input() for _ in range(3)]
ans = 0
for a, b, c in zip(*S):
    x = len({a, b, c})
    if x==2: ans+=1
    if x==3: ans+=2
print(ansk)
