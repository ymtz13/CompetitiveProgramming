N = int(input())
ST = [tuple(input().split()) for _ in range(N)]
ans = sorted([(-int(T), S) for S, T in ST])[1][1]
print(ans)
