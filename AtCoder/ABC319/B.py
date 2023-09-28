N = int(input())
ans = []
for i in range(N + 1):
    a = "-"
    for j in range(1, 10):
        if N % j:
            continue
        d = N // j
        if i % d:
            continue
        a = str(j)
        break

    ans.append(a)

print("".join(ans))
