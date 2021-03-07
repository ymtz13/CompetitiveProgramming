N = int(input())
P = list(map(int, input().split()))
L = [False]*(200001)
i = 0

for p in P:
    L[p] = True
    while L[i]: i+=1
    print(i)
