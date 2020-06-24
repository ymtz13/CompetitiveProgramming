A, B, K = list(map(int, input().split()))
C = [i for i in range(1, min(A,B)+1) if A%i==0 and B%i==0]
print(C[-K])
    
