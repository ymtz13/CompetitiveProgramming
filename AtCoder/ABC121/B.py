N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))

z = 0
for n in range(N):
    x = C
    A = list(map(int, input().split()))
    for a,b in zip(A,B):
        x += a*b

    if x>0 : z+=1

print(z)
