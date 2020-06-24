K, A, B = list(map(int, input().split()))
print(((K-A+1)//2)*(B-A)+(K-A+1)%2+A if B-A>2 else K+1)
