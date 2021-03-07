N, A, B = map(int, input().split())
print(B*min(N,5)+A*max(N-5,0))