def replacer(string, old_sub_str, new_sub_str):
    new_str = string.replace(old_sub_str, new_sub_str)
    return new_str


string = input('Строка: ') or '11 23 44 55 23 22'
old_sub_str = input('Ее заменяемая подстрока: ') or '23'
new_sub_str = input('Новая подстрока: ') or '!!!'
print(replacer(string, old_sub_str, new_sub_str))
