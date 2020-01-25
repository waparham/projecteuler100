#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
limit = 10001
prime_nums = [2]
num = 1
count = 0

while len(prime_nums) < limit:
    num += 1
    for primes in prime_nums:
        if num % primes == 0:
            count += 1
            break
    if num not in prime_nums and count == 0:
        count = 0
        prime_nums.append(num)
    else:
        count = 0
            
print('The '+str(limit)+'th prime number is '+str(prime_nums[-1]))