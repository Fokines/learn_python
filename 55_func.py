def my_func():
    '''Строка документации
    Должно описывать, что делает функция, что означают ее параметры и какое значение она возвращает
    '''
    
def keywords(first = 1, second = 2): #значения по умолчанию используются если при вызове не было передано никаких фактических значений
    '''Присваиваем значения по усолчанию'''
    print(f"first: {first}")
    print(f"second: {second}")
    
keywords()

def return_one():
    '''Возвращает 1'''
    return 1

print(return_one())

def double(input):
    return input * 2

def triple(input):
    return input * 3

functions = [double, triple]
for function in functions:
    print(function(3))