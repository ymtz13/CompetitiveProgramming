N = int(input())
n = 2
isPrime = True
while n*n<=N and isPrime:
    isPrime = N%n>0
    n+=1
print('YES' if isPrime else 'NO')
