N = int(input())
for x in range(0, 101, 5):
    d = abs(N - x)
    if d <= 2:
        print(x)
