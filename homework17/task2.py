string = input('Введите строку: ') or 'I am learning Python. hello, WORLD!'

s = string[string.find('h') + 1:string.rfind('h')]

print(string[:string.find('h') + 1] + s[::-1] + string[string.rfind('h'):])
