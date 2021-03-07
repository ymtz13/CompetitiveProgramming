C = int(input())
X = [sorted(tuple(map(int, input().split()))) for _ in range(C)]
K = [max([x[i] for x in X]) for i in range(3)]
print(K[0]*K[1]*K[2])
