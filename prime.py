import math
def is_prime(n):
    ans = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = False
    return ans
print("Nonprime numbers between 1 to 100:")
for x in filter(is_prime, range(1, 25)):
    print(x)
