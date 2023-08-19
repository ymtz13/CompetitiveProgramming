T = int(input())
Ans = []

X = [2, 3, 5, 7, 11, 13, 17, 19, 23]
D = 223092870

for _ in range(T):
    N = int(input())
    d = D
    for i in range(N):
        for j, x in enumerate(X):
            if i & (1 << j):
                d //= x


for ans in Ans:
    print(ans)
