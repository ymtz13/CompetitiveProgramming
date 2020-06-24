N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
print(sum(A[0::2])*2-sum(A))
