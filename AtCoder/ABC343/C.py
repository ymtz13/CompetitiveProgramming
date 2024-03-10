N = int(input())

for x in range(1, N + 1):
    x3 = x * x * x
    if x3 > N:
        break

    s = str(x3)
    if s == s[::-1]:
        ans = x3


print(ans)
