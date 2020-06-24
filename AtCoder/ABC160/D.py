N, X, Y = map(int, input().split())
ans = [0]*N
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if i<X:
            if j<X:
                ans[j-i]+=1
            elif j<=Y:
                ans[X-i+min(j-X, Y-j+1)]+=1
            else:
                ans[X-i+j-Y+1]+=1
        elif i<=Y:
            if j<=Y:
                ans[min(j-i, i-X+Y-j+1)]+=1
            else:
                ans[min(i-X+1, Y-i)+j-Y]+=1
        else:
            ans[j-i]+=1

for a in ans[1:]:
    print(a)
