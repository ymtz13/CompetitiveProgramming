N, Q = list(map(int, input().split()))
S = input()

n = [0]
for i in range(1,len(S)):
    n.append(n[-1])
    if S[i-1:i+1]=='AC': n[-1] += 1

for q in range(Q):
    l, r = list(map(int, input().split()))
    print(n[r-1]-n[l-1])
