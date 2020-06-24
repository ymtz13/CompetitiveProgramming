N = int(input())
D, X = list(map(int, input().split()))
for _ in range(N):
    X += (D-1)//int(input())+1
print(X)
