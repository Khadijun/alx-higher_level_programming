#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
print('Last digit of {} is {}'.format(number, number % 10), end=' ')
if number < 6 and number > 0:
    print('and is less than 6 and not 0')
elif number > 5:
    print('and is greater than 5')
else:
    print('and is 0')
