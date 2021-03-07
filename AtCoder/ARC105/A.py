X = list(map(int, input().split()))

ans = 'No'
for i in range(4):
    if X[i]*2==sum(X): ans = 'Yes'

for i in range(1,4):
    if (X[0]+X[i])*2==sum(X): ans = 'Yes'

print(ans)
