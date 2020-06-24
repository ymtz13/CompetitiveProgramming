s = set()
for i in range(1,10):
    for j in range(i, 10):
        s |= {i*j}
print('Yes' if int(input()) in s else 'No')
