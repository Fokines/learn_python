name = 'bill monroe'
print(name.capitalize())
print(name.upper())
print(name.title())
print(name.swapcase())
name = 'BILL MONROE'
print(name.lower())

print("William".startswith('W'))
print("William".startswith('Bill'))
print("Molly".endswith('olly'))
print("abc123".isalnum())
print("abc123".isalpha())
print("abc".isalnum())
print("123".isnumeric())
print("Sandy".istitle())
print("Sandy".islower())
print("SANDY".isupper())
print('{1} comes after {0}, but {1} comes before {2}'.format('first', 'second', 'third'))
print('{country} is an island. {country} is off of the coast of {continent} in the {ocean}'''.format(ocean='Indian Ocean', continent='Africa', country='Madagascar'))
values = {'first': 'Bill', 'last': 'Bailey'}
print("Won't you come home {first} {last}?".format(**values))
text = "|{0:>22}||{0:<22}|"
print(text.format('O', 'O'))
text = "|{0:<>22}||{0:<>22}|"
print(text.format('O', 'O'))
count = 55
print(f"|{count:6d}")