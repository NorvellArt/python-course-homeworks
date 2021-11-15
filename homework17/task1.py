string = input('Введите строку: ') or 'I am learning Python. hello, WORLD!'

print(string[:string.find('h')] + string[string.rfind('h'):])
