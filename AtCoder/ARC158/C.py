N = int(input())
A = sorted(list(map(int, input().split())))

ans = 0
for a in A:
    ans += sum(map(int, list(str(a)))) * N * 2

for i in range(1, 20):
    t = 10**i
    B = sorted([-1] + [a % t for a in A] + [t])
    # print(t, B)

    j = len(B)
    for b in B[1:-1]:
        while B[j - 1] + b >= t:
            j -= 1

        c = len(B) - j - 1
        # print(b, c)
        ans -= c * 9


print(ans)
