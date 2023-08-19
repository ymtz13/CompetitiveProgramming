N = int(input())
A = list(map(int, input().split()))

ans = [a for a in A if a % 2 == 0]
print(*ans)
