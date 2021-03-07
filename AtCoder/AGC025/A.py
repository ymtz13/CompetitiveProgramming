ans = 10000000
N = int(input())
for A in range(1, N//2+1):
    B = N-A
    ans = min(ans, sum(map(int, str(A))) + sum(map(int, str(B))))
print(ans)