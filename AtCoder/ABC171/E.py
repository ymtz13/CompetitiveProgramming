N = int(input())
A = list(map(int, input().split()))
sA = 0
for a in A:
    sA ^= a

ans = [sA^a for a in A]
print(' '.join(map(str, ans)))
