N = int(input())
A = sorted(list(enumerate(map(int, input().split()))), key=lambda x: x[1])
print(A[-2][0] + 1)
