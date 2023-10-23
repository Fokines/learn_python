items = [[0, 'a', 2], [5, 'b', 0], [2, 'c', 1]]
print(sorted(items)) #по умолчанию механизм сортировки выполняет сравнение по первым элементами подсписков
#для другой сортировки нужно описать метод, возвращающий, например, второй элемент и передавать его в параметр key функции сортировки
def second(item):
    return item[1]

print(sorted(items, key=second))
print('\n')
#благодаря lambda можно сделать то же самое без полноценного описания функции
#синтаксис lambda <Параметр>: <Возвращаемое значение>

print(sorted(items, key = lambda item: item[1]))
print(sorted(items, key = lambda item: item[2]))