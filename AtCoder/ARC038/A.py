N = int(input())
A = sorted(list(map(int, input().split())))[::-1]
print(sum(A[::2]))
