import re

text = open('take_numbers_regex.txt', 'r').read()

numbers = re.findall('[0-9]+', text)

total = sum([int(num) for num in numbers])


print(total)