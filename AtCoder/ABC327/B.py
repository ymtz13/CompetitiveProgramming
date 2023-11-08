B = int(input())
for A in range(1, 19):
    if pow(A, A)==B:
        print(A)
        exit()
print(-1)
