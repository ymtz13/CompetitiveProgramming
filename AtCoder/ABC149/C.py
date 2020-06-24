X = int(input())
while True:
    isPrime = True
    f = 2
    while f*f<=X and isPrime:
        if X%f==0: isPrime=False
        f+=1
    if isPrime:
        print(X)
        exit()
    X+=1
