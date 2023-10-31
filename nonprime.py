import math
def is_not_prime(n):
    ans = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = True
    return ans
print("Nonprime numbers between 1 to 100:")
for x in filter(is_not_prime, range(1, 25)):
    print(x)
