N = int(input())
for A in range(1, 100):
    X = pow(3, A)
    if X>N: break
    for B in range(1, 100):
        Y = pow(5, B)
        if X+Y>N: break
        if X+Y==N:
            print(A,B)
            exit()

print(-1)