N = int(input())
A = list(map(int, input().split()))
i = 1
ans = 0
for a in A:
    if a==i: i+=1
    else: ans +=1
print(ans if ans<N else -1)
