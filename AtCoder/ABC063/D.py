N, A, B = list(map(int, input().split()))
H = [int(input()) for _ in range(N)]

C = A-B
j = sum([h//C for h in H])
H_broken = []
for i, m in enumerate(sorted([h%C for h in H])):
    h_broken = m+(j//N+1)*C if i<j%N else m+(j//N)*C
    H_broken.append(h_broken)

H_broken = H_broken[j%N-1::-1] + H_broken[-1:j%N-1:-1]
print(H_broken)

D = B*N+C
M = (H_broken[-1]//D)*N

for i in range(N):
    if H_broken[i]%D <= i*B: break
    M += 1

print(M)

# m1 <= ... <=  mj <= ... <= mk <= ... <= mn < C
# 
# (3C + mj) - (2C + mk) = C + mj - mk
# -C+1 <= mj-mk <= 0
# 1 <= (3C + mj) - (2C + mk) = C + mj - mk <= C


# 8 7 4 2 -> j = (3+3+2+1) = 9
# 0 0 0 1
# 3 3 2 2
# 6 6 4 5


# 3 100 1
# 100 1 1
# 1 1 1
#

# 28: 8 8 8 3
# 17: 8 3 3 3
#  9: 3 3 3 3
#  1: 3 3 3 3


# 28 17  9  1
# 13 12 14 16
#  1  1  1  1
