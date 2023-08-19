N = int(input())
A = list(map(int, input().split()))
A.sort()

S = sum(A)
X = S // N
R = S - X * N
G = [X] * (N - R) + [X + 1] * R


ans = 0
for a, g in zip(A, G):
    ans += abs(a - g)
ans //= 2

print(ans)
