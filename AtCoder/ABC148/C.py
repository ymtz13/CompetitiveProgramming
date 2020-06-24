A, B = list(map(int, input().split()))
ans = A*B
if A>B: A,B = B,A
while A:
    A, B = B%A, A
print(B)
print(ans//B)
