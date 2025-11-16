# What this code outputs and why? (Anki)
"""
Второй аргумент метода dictionary get определяет,
что возвращать при отсутствии ключевого слова. По умолчанию возвращается None.
"""
x = {'a':0, 'b':1}
y = x.get('c', 'default')
print(y) # default
