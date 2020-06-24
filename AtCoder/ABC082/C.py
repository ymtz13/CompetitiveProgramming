N = int(input())
A = list(map(int, input().split()))
B = {}
for a in A:
    if a not in B: B[a] = 0
    B[a]+=1

ans = 0
for k,v in B.items():
    ans += v if v<k else v-k
print(ans)
