import itertools
n=input("Enter the number")
P=list(itertools.permutations(n))
print(*["".join(p) for p in P])
