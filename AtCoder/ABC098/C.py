N = int(input())
S = input()
ne_r = S.count('E')
nw_l = 0
ans = N
for i,c in enumerate(S):
    if c=='E': ne_r-=1
    ans = min(ans, ne_r + nw_l)
    if c=='W': nw_l+=1
print(ans)
