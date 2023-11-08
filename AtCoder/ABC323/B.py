N = int(input())
S = [(-input().count("o"), i) for i in range(1, N + 1)]
S.sort()

print(*[i for _, i in S])
