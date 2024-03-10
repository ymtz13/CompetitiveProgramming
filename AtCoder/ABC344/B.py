A = []
while True:
    A.append(int(input()))
    if A[-1] == 0:
        break

for a in A[::-1]:
    print(a)
