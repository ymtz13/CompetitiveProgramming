N, D = list(map(int, input().split()))
k = 1 if N%(2*D+1) >0 else 0
print(N//(2*D+1)+k)
