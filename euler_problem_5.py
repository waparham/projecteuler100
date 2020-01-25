# What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?
d = 20
d_range = range(1, d + 1)
n = 0
for d in d_range:
    n += 1
    if n % d == 0:
        count += 1
