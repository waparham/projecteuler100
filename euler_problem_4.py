#Find the largest palindrome made from the product of two 3-digit numbers.  
x = 100
y = 100
z = 0
p_list = []
while x < 1000 and y < 1000:
    z = x * y
    zstr = str(z)
    if zstr == zstr[::-1]:
        p_list.append(z)
    x += 1
    if x == 1000:
        y +=1
        x = 0
p_list.sort()
print(p_list[-1])