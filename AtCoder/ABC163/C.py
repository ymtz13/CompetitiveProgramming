N = int(input())
A = list(map(int, input().split()))
X = [0]*N
for a in A:
    X[a-1]+=1

for x in X:
    print(x)
