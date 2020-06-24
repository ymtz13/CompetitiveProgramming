def test(x):
    n=0
    while x%2==0:
        x//=2
        n+=1
    return n

N = input()
print(min(map(test, map(int, input().split()))))
