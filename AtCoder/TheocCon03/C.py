N, M = list(map(int, input().split()))
a = min(N, M//2)
b = (M-a*2)//4
print(a+b)
