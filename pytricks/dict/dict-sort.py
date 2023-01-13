# PyTricks 2023-01-12
# How to sort a Python dict by value

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))

# Or:
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
