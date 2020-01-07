#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
y = 1
x = 1
z = 0
while x + y < 4000000:
    y = x + y
    if y % 2 == 0:
        z = z + y
    else:
        continue
    x = x + y
    if x % 2 == 0:
        z = z + x
    else:
        continue
print(str(z))