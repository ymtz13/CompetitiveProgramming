N = input()
W = list(input().split())

for w in ("and", "not", "that", "the", "you"):
    if w in W:
        print("Yes")
        exit()

print("No")
