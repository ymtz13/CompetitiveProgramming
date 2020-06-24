N = int(input())
W = [input() for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if W[i]==W[j]:
            print('No')
            exit()

    if W[i][-1]!=W[i+1][0]:
        print('No')
        exit()

print('Yes')

