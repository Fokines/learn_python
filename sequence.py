print(2 in [1, 2, 3])

print('a' not in 'cat')

print(10 in range(12))

print(10 not in range(2, 4))

my_sequence = 'Bill Cheatham'
print(my_sequence[0])
print(my_sequence[2])
print(my_sequence[12])

print('\n\n')

print(my_sequence[-1])
print(my_sequence[-2])
print(my_sequence[-13])

print('\n\n')

print(my_sequence.index('C'))
print(my_sequence.index('a'))

#ищем симлов 'а' в слова между 9 и 12 (невключительно) буквой
print(my_sequence.index('a', 9, 12))


my_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(my_sequence[2:5])
print(my_sequence[:5])
print(my_sequence[3:])
print(my_sequence[-6:])

print('\n\n')


my_sequence = [1, 2, 3, 4, 5, 6, 7]
print(len(my_sequence))
print(min(my_sequence))
print(max(my_sequence))
print(my_sequence.count(1))


# о списках
my_list = list("Henry Miller") #создание списка из строки
print(my_list)

pies = ['cherry', 'apple']
print(pies)
pies.append('rhubarb') #добавляет новый эл. в список (с конца)
print(pies)
pies.insert(1, 'cream') #вставляет новый эл. на N место в списке
print(pies)
desserts = ['cookies', 'paste']
desserts.extend(pies) #добавление pies к desserts с конца
print(desserts)
print('\n\n')
print(desserts.pop()) #в pop() можно передать индекс элемента. по умолчанию - последний элемент
print(desserts)

pies.remove('apple') #удаляет первое вхождение элемента в список
print(pies)