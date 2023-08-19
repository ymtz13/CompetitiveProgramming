N, M, D = map(int, input().split())

A = [-D - 5] + list(map(int, input().split()))
B = [-D - 5] + list(map(int, input().split()))
A.sort()
B.sort()

i = 0
ans = -1

for a in A:
    while i + 1 < len(B) and B[i + 1] <= a + D:
        i += 1
    if abs(a - B[i]) <= D:
        ans = max(ans, a + B[i])

print(ans)
