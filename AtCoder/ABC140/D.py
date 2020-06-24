N, K = list(map(int, input().split()))
S = input()

repulsion_end = 0
if S[ 0]=='L': repulsion_end+=1
if S[-1]=='R': repulsion_end+=1

repulsion = 0
back2back = 0
for i in range(N-1):
    if S[i]=='R' and S[i+1]=='L': repulsion+=1
    if S[i]=='L' and S[i+1]=='R': back2back+=1

remove_repulsion = min(K, back2back, repulsion)
back2back -= remove_repulsion
K -= remove_repulsion
repulsion -= remove_repulsion

if K>0 and back2back>0:
    unhappy=1
elif K>0 and repulsion>0 and repulsion_end<2:
    repulsion_end += 1
    repulsion -=1
    unhappy=repulsion*2+repulsion_end
else:
    unhappy=repulsion*2+repulsion_end

print(N-unhappy)
