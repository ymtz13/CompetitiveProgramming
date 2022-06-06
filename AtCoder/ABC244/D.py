D = {
    'R G B': +1,
    'G B R': +1,
    'B R G': +1,
    'G R B': -1,
    'B G R': -1,
    'R B G': -1,
}

S = input()
T = input()

print('Yes' if D[S] == D[T] else 'No')
