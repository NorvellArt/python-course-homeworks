str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'


def replacer(string, old_text, new_text, replace_number):
    """
    Находит и заменяет слово.

    Введите строку, слово, которое нужно заменить, слово, на которое нужно заменить и номер совпадения,
    с которого нужно начать замену.
    Длины старого и нового слова должны быть одинаковыми.
    :param string: строка. Строка в которой будет производиться поиск и замена
    :param old_text: строка. Слово, которое нужно заменить
    :param new_text: строка. Слово, которое заменит старое слово
    :param replace_number: целое число. Номер совпадения, с которого начать замену.
    :return: строка. Возвращает преобразованную строку.
    """
    if len(old_text) == len(new_text):
        # Нахождение индесков совпадений
        indices = [i for i in range(len(string) - len(old_text) + 1) if string[i:i + len(old_text)] == old_text]
        print(indices)
        if len(indices) < replace_number:
            raise AttributeError('Вы ввели число больше, чем число совпадений.')
        # Превращение строки в список для замены
        string = list(string)
        # Цикл для замены последующих совпадений
        while replace_number <= len(indices):
            # Находит в списке string буквы по индексам и заменяет их новым словом
            string[indices[replace_number - 1]:indices[replace_number - 1] + len(
                old_text)] = new_text
            replace_number += 1
        # Превращает массив букв обратно в строку и возвращает её
        return ''.join(string)
    else:
        raise AttributeError('Длина нового слова должна быть равной длине старого.')


str2 = replacer(str1, 'Nuthon', 'Python', 2)
print(str2)
