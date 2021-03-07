A, B = map(lambda x: abs(int(x)), input().split())
print('Ant' if A<B else 'Bug' if A>B else 'Draw')