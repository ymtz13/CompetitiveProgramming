A, B, C = list(map(int, input().split()))
if A>B: A,B=B,A
while A:
    A,B = B%A, A
print('YES' if C%B==0 else 'NO')
