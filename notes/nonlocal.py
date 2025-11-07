x = 5

def credits():
    x = 2
    def money():
        nonlocal x # обращается к внешней х, но не к глобальной
        print(f'Balance is: {x}')
        x += 30000
        print(f'Money was updated! Inner balance: {x}')

    money()
    print(f'Outer balance: {x}')

credits()
print(x)