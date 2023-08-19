A = list(map(int, input().split()))
b = 1
ans = 0
for a in A:
    ans += b * a
    b *= 2

print(ans)
