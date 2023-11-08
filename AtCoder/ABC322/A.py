N = int(input())
S = input()

if "ABC" not in S:
    print(-1)
    exit()

print(S.index("ABC") + 1)
