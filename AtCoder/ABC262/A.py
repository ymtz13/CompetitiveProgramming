Y = int(input())
for i in range(4):
  if (i + Y) % 4 == 2:
    print(i + Y)
    exit()
