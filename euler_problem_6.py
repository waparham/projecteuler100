#The difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
limit = 100
sum_squares = []
squares_sum = []

for i in range(1, limit + 1):
    sum_squares.append(i ** 2)
    squares_sum.append(i)
    val_sum_squares = sum(sum_squares)
    val_squares_sum = sum(squares_sum) ** 2
    difference = val_squares_sum - val_sum_squares 
print('The difference between the sum of the squares of the first ' + str(limit) + ' natural numbers and the square of the sum is ' + str(difference))
