N = int(input())

ans = 0
while N % 2 == 0:
    ans += 1
    N //= 2

print(ans)
