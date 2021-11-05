N, M = map(int, input().split())
C = [0]*N
for _ in range(M):
  A, B = map(int, input().split())
  C[max(A, B)-1] += 1
print(len(tuple(filter(lambda c: c==1, C))))
