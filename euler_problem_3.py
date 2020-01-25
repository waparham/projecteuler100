#What is the largest prime factor of the number 600851475143 ?
x = 600851475143
i = 0
factors = []
f = 1
while f < x:
    i += 1
    if x % i == 0:
        factors.insert(0, i)
        f = f * i
else:
    print(factors)
    print(factors[0])