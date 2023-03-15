N = int(input())
ans = sum([n for n in range(N) if n%3==0 or n%5==0])
print(ans)
