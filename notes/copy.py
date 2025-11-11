# What this code outputs and why?

# c = copy.copy(b) эквивалент c = b[:] и создаёт поверхностную копию.
# copy.copy() можно использовать для любых объектов, не только для списков.
# В библиотеки есть copy.deepcopy(), которая делает глубокую копию вложенных объектов.

import copy

a = [1]
b = [0, a]
c = copy.copy(b)

print(c is b)
print(c[1] is b[1] is a)