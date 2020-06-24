A, B = map(int, input().split())

for p in range(1, 101):
    if p*108//100-p==A and p*110//100-p==B:
        print(p)
        exit()
print(-1)
