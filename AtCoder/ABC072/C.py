N = int(input())
A = list(map(int, input().split()))
M = [0]*(10**5+10) # M[0] <--> X=-1   ==> M[X+1]
for a in A:
    for i in range(3): M[a+i]+=1
print(max(M))
