N = int(input())
S = [input() for _ in range(N)]

for i, si in enumerate(S):
    for j, sj in enumerate(S):
        if i == j:
            continue
        s = si + sj
        if s == s[::-1]:
            print("Yes")
            exit()

print("No")
