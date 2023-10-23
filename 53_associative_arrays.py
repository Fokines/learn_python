map = dict() #пустой ассоциативный массив
print(type(map))
print(map)

kv_list = [['key-1', 'value-1'], ['key-2', 'value-2']]
print(dict(kv_list)) #преобразование списка в ассоц. массив

map = {'key-1': 'value-1', 'key-2': 'value-2'}
print(map)

print('\n')
print(map['key-1']) #обращение по ключу и получение значения
print('\n')

#добпавление нового ключ-значения
map['key-3'] = 'value-3'
print(map)
print('\n')

#проверка есть ли определенный ключ
if 'key-4' in map:
    print(map['key-4'])
else:
    print('key-4 not there')
    
print('\n')

map.get('key-4', 'default-value') #добавление нового ключ-значения

del(map['key-1']) #удаление ключ-значения
print(map)
print('\n')
print(map.keys()) #ключи
print(map.values()) #значения
print(map.items()) #пары
for key, value in map.items():
    print(f"{key}: {value}")
    
letters = 'abcde'
cap_map = {x: x.upper() for x in letters}
print(cap_map['b'])
