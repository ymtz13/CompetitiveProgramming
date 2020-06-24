N = int(input())
X, R = [], []
for _ in range(N):
    s = input().split()
    X.append(int(s[0]))
    R.append(int(s[1]))

if N>2:
    print('X(')

l=abs(X[0]-X[1])
R1, R2 = min(R[0], R[1]), max(R[0],R[1])
R1=R1-l


print(max(R_,R1,R2))
