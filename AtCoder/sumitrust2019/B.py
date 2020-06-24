N = int(input())
ans = -1
for X in range(1, N+1):
    if str(X*108)[:-2]==str(N): ans = X
    
print(ans if ans>-1 else ':(')
