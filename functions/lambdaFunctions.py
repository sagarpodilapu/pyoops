# anonymous function
# single line function
# lambda arguments: expression
import random

double = lambda x: x * 2
print(double(5))

randomlist = random.sample(range(10, 300), 8)

odd_numbers = list(filter(lambda x: (x % 2 == 1), randomlist))
print(randomlist)
odd_numbers.sort()
print(odd_numbers)

multiply = list(map(lambda x: (x * 2), randomlist))
print(multiply)
