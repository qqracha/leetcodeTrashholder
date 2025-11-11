# What this code outputs and why?
# Shallow copy - поверхностная копия

a = [1]
b = [0, a]
c = b[:]

print(c is b) # False
# 'c' и 'b' — два разных списка, потому что b[:] создаёт поверхностную копию. Копия это новый список, который содержит те же ссылки на объекты.

print(c[1] is b[1] is a) # True
# Мы обращаемся напрямую к объектам внутри массива и сравниваем их, shallow copy копирует ссылки на объекты

# c = b[:] created a shallow copy, so c and b are not the same object. Both still reference a.