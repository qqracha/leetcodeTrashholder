# Second argument of the dictionary get method specifies
# what to return when there is no keyword. By default it returns None
x = {'a':0, 'b':1}
y = x.get('c', 'default')
print(y)
