N = int(input())
H = list(map(int, input().split()))
MSE = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:x[2])


