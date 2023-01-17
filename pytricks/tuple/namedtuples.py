# PyTricks 2023-01-17
# Using namedtuple is way shorter than defining a class manually.

from collections import namedtuple

# Our new "Car" class works as expected
Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)

print(my_car)

# Like tuples, namedtuples are immutable
# my_car.color = 'blue'
