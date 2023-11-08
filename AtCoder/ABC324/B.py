N = int(input())

for x in range(100):
    r = 2**x
    if r > N:
        break
    for y in range(100):
        if r == N:
            print("Yes")
            exit()

        r *= 3
        if r > N:
            break

print("No")
