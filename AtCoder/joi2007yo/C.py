S = [ord(c) - ord("A") for c in input()]
T = [(c - 3) % 26 for c in S]
U = [chr(c + ord("A")) for c in T]
print(*U, sep="")
