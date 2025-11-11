# What this code outputs and why?
# c = copy.deepcopy(b) creates a deep copy of b, duplicating any internal references. c[1] no longer points to a
# Deepcopy создаёт новый список и рекурсивно копирует все вложенные объекты, а не создаёт ссылки на объекты.

import copy

a = [1]
b = [0, a]
c = copy.deepcopy(b) # Создает глубокую копию 'b', но при сравнении всё равно является копией.

print(c is b) # False. 'c' является копией, хоть и глубокой.
print(c[1] is b[1] is a) # False. Внутри Deepcopy копии объектов, а не ссылки на них.

a[0] = 'X'
c[1][0] = 'Y'

print(b)  # Изменяем оригинальный список 'a' (и, следовательно, b[1]) || [0, ['X']]
print(c) # Изменяем копию внутри 'c' || [0, ['Y']]