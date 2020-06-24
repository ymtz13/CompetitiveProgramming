S = list(map(int, input()[::-1]))

R=[0]
r=0
k=1
for c in S:
    r = (r+k*c) % 2019
    k = k*10 % 2019
    R.append(r)
    
N = [0]*2019
ans = 0
for r in R:
    ans += N[r]
    N[r] += 1
print(ans)
