y = 0
for x in range(1000):
    if x % 3 == 0:
        y = y + x
        print(str(x))
    elif x % 5 == 0:
        y = y + x
    else:
        continue
else:
    print('The sum is ' + str(y))