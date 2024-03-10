N = int(input())
s = 0
for _ in range(N):
    X, Y = map(int, input().split())
    s += X - Y

print("Draw" if s == 0 else "Takahashi" if s > 0 else "Aoki")
