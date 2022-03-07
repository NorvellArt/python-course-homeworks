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
    @add_title(' Редактирование данных каталога фильмов ')
    def wait_user_answer(self):
        print('Действия с фильмами:')
        print('1 - добавление фильма'
              '\n2 - каталог фильмов'
              '\n3 - просмотр определенного фильма'
              '\n4 - удаление фильма'
              '\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @add_title(' Добавление фильма: ')
    def add_user_films(self):
        dict_films = {
            'название фильма': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None
        }
        for key in dict_films:
            dict_films[key] = input(f'Введите {key} фильма: ')
        return dict_films

    @add_title(' Список фильмов: ')
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f'{ind}. {film}')

    @add_title(' Ввод названия фильма: ')
    def get_user_film(self):
        get_user_film = input('Введите название фильма: ')
        return get_user_film

    @add_title('Просмотр фильма')
    def show_single_film(self, film):
        for key in film:
            print(f'{key} фильма - {film[key]}')

    @add_title('Сообщение об ошибке')
    def show_incorrect_film_title(self, film_title):
        print(f'Фильма с названием {film_title} не существует')

    @add_title('Удаление фильма: ')
    def remove_single_film(self, film):
        print(f'Фильм "{film}" - был удален')

    @add_title('Сообщение об ошибке')
    def show_incorrect_answer_error(self, answer):
        print(f'Варианта {answer} не существует')
