
# L =[]
# S = [7,5,3]


# n = 7
# L = [7]

# e = 7->11, m = 11
#


N, M = list(map(int, input().split()))
F = [[] for _ in range(N)]
T = [[] for _ in range(N)]
for i in range(M):
    A, B = list(map(int, input().split()))
    F[A-1].append(B-1)
    T[B-1].append(A-1)

print(T)
L = []
S = [i for i in range(N) if len(T[i])==0]

print(S)
