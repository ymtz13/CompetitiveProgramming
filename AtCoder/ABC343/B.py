N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    print(*[i for i, a in enumerate(A, 1) if a])
