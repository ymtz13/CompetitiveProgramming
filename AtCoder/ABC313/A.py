N = int(input())
P = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

print(max(0, max(P[1:]) + 1 - P[0]))
