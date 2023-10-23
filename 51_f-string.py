from string import Template

#f-строки аналогичны методу format, но более понятный
a = 1
b = 2
print(f"a is {a}, b is {b}. adding them results in {a + b}")
test = 99
print(f"|{test:10d}")

#подстановка значений 
greeting = Template("$hello Mark")
print(greeting.substitute(hello="Moi moi"))
