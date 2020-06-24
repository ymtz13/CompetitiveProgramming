A, B = list(map(int, input().split()))

print(100,100)
for r in range(50):
    if r%2==1: print('#'*100)
    else:
        for c in range(100):
            if c%2==0 and A>1:
                print('.', end='')
                A-=1
            else:
                print('#', end='')
        print()

for r in range(50):
    if r%2==0: print('.'*100)
    else:
        for c in range(100):
            if c%2==0 and B>1:
                print('#', end='')
                B-=1
            else:
                print('.', end='')
        print()

            
