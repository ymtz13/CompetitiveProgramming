N, A, B, C = list(map(int, input().split()))
L = [int(input()) for _ in range(N)]

assign = [0]*N

cost_min = 10000

while assign.count(3)<N:

    NL = [0]*4
    XL = [0]*4
    for i in range(N):
        NL[assign[i]] += 1
        XL[assign[i]] += L[i]

    if min(NL[:3])>=1:
        cost = (sum(NL[:3])-3)*10 + abs(A-XL[0]) + abs(B-XL[1]) + abs(C-XL[2])
        cost_min = min(cost_min, cost)

    for i in range(N):
        if assign[i]<3:
            assign[i] += 1
            for j in range(i):
                assign[j] = 0
            break

print(cost_min)
