for i in range(10):
    x = i * 2
    print(x)

print('\n\n')

for i in range(10):
    x = i * 2
    if x == 4:
        continue #пропускает один шаг в цикле и переходит к след. итерации
    print(x)

count = 0
while count < 3:
    print(f"the count is {count}")
    count += 1


print('\n\n')
count = 0
while True:
    print(f"the count is {count}")
    if count > 5:
        break
    count += 1