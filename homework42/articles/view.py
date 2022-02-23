def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, "="))
            res = func(*args, **kwargs)
            print("=" * 50)
            return res

        return wrapper

    return decorator


class UserInterface:
    @add_title(' Ввод пользовательских данных ')
    def wait_user_answer(self):
        print('Действия со статьями:')
        print('1 - создание статьи'
              '\n2 - просмотр статей'
              '\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @add_title(' Создание статьи: ')
    def add_user_articles(self):
        dict_article = {
            'название': None,
            'автор': None,
            'количество страниц': None,
            'описание': None
        }
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        return dict_article

    @add_title(' Список статей: ')
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f'{ind}. {article}')
