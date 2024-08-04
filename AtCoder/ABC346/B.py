W, B = map(int, input().split())
N = W + B

S = "wbwbwwbwbwbw" * 200

A = [0]
for c in S:
    A.append(A[-1] + (1 if c == "w" else 0))

for f in range(30):
    t = f + N

    nW = A[t] - A[f]
    if nW == W:
        print("Yes")
        exit()

print("No")
