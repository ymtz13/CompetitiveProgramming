N = int(input())
streak = 0
max_streak = 0
for _ in range(N):
    D1, D2 = input().split()
    if D1==D2:
        streak += 1
        max_streak = max(max_streak, streak)
    else:
        streak = 0

print('Yes' if max_streak>=3 else 'No')
