M = int(input())
D = list(map(int, input().split()))

K = (sum(D) + 1) // 2

for m, d in enumerate(D, 1):
    if K <= d:
        print(m, K)
        exit()
    K -= d
