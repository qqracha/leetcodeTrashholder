class Colors:
    def dark(self):
        return 'black'
    
class Tea(Colors): # class 'Tea' наследует методы и атрибуты родительского класса 'Colors' 
    def __init__(self): # создаём объект (self) и через объект вызываем метод класса (dark)
        print(f"Current tea is {self.dark()}")

Tea()    
