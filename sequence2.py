squares = []

for i in range(10):
    squared = i*i
    squares.append(squared)

print(squares)

#списковое включение того же самого кода
squares = [i*i for i in range(10)]

print(squares)

squares = [i*i for i in range(10) if i%2 == 0]
print(squares)

my_list = list()
print(str(my_list))

multi_line = """This is a
multi-line string,
which includes linebreaks"""
print(multi_line)

input = " I want more "
input.strip()
print(input)

output = 'Barry'
print(output.ljust(10)) #добавит 10 символов в конце
print(output.rjust(10, '*'))

text = "mary nad a lamb"
print(text.split()) #разбивает строку на список со словами. по умолчанию по пробелу

items = ['cow', 'milk', 'butter'] # строка из списка и посреди элементов строка-разделитель
print(" and ".join(items))

