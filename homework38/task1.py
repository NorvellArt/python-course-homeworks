from typing import Dict
import json

countries: Dict[str, str] = {
    'Россия': 'Москва',
    'Казахстан': 'Нур-Султан',
    'Беларусь': 'Минск',
    'Украина': 'Киев',
    'Киргизия': 'Бишкек',
}


def user_choice() -> int:
    print('Выбор действия')
    print('1 - добавление данных')
    print('2 - удаление данных')
    print('3 - поиск данных')
    print('4 - редактирование данных')
    print('5 - сохранение данных')
    print('6 - просмотр данных')
    print('0 - выключение программы')
    return int(input('Введите число: '))


def service(num: int) -> None:
    def add_country(country: str, capital: str) -> None:
        if country.lower() in [country.lower() for country in countries.keys()]:
            print('\nТакая страна уже есть в списке.\n')
            service(user_choice())
        else:
            countries[country] = capital
            print('\nСтрана успешно добавлена.\n')

    def delete_country(country: str) -> None:
        if country.lower() not in [country.lower() for country in countries.keys()]:
            print('\nТакой страны нет в списке.\n')
            service(user_choice())
        else:
            countries.pop(country)
            print('\nСтрана успешно удалена.\n')

    def search_country(country: str) -> None:
        if country.lower() in [country.lower() for country in countries.keys()]:
            print(f'\nСтрана {country} есть в списке. Столица: {countries.get(country)}\n')
            service(user_choice())
        else:
            print('\nТакой страны нет в списке.\n')

    def edit_country(country: str, capital: str) -> None:
        if country.lower() in [country.lower() for country in countries.keys()]:
            countries[country] = capital
            print('\nДанные успешно обновлены.\n')
            service(user_choice())
        else:
            print('\nТакой страны нет в списке.\n')

    def save_countries(countries: Dict[str, str]) -> None:
        try:
            data: Dict[str, str] = json.load(open('countries.json'))
        except FileNotFoundError:
            data = {}
        data.update(countries)
        with open('countries.json', 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            print('\nДанные успешно сохранены.\n')

    def load_countries():
        with open('countries.json', 'r') as f:
            print(json.load(f))

    if num == 1:
        country = input('Введите страну, которую хотите добавить: ')
        capital = input('Введите ее столицу: ')
        add_country(country, capital)
        service(user_choice())
    if num == 2:
        country = input('Введите страну, которую хотите удалить: ')
        delete_country(country)
        service(user_choice())
    if num == 3:
        country = input('Введите страну, которую хотите найти: ')
        search_country(country)
        service(user_choice())
    if num == 4:
        country = input('Введите страну, которую хотите изменить: ')
        capital = input('Введите столицу, которую хотите изменить: ')
        edit_country(country, capital)
        service(user_choice())
    if num == 5:
        save_countries(countries)
    if num == 6:
        load_countries()
    if num == 0:
        print('\nВыключение программы.\n')


service(user_choice())
