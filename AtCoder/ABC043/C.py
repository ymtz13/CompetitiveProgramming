N = int(input())
A = list(map(int, input().split()))
ans = 10**10
for y in range(-100, 101):
    cost = sum([(x-y)*(x-y) for x in A])
    ans = min(ans, cost)
print(ans)
