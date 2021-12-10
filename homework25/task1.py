class Book:
    name = 'Название книги'
    year = 'Год издательства'
    publisher = 'Издатель'
    genre = 'Жанр'
    author = 'Автор'
    price = 'Цена'

    def print_book_info(self):
        print(f"Информация о книге".center(40, '*'))
        print(f'Название книги: {self.name}')
        print(f'Год издательства: {self.year}')
        print(f'Издатель: {self.publisher}')
        print(f'Жанр: {self.genre}')
        print(f'Автор: {self.author}')
        print(f'Цена: {self.price}')
        print('=' * 40)

    def input_info(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_name(self):
        print(self.name)

    def set_name(self, value):
        self.name = value

    def get_year(self):
        print(self.year)

    def set_year(self, value):
        self.year = value

    def get_publisher(self):
        print(self.publisher)

    def set_publisher(self, value):
        self.publisher = value

    def get_genre(self):
        print(self.genre)

    def set_genre(self, value):
        self.genre = value

    def get_author(self):
        print(self.author)

    def set_author(self, value):
        self.author = value

    def get_price(self):
        print(self.name)

    def set_price(self, value):
        self.name = value


b1 = Book()
b1.print_book_info()
b1.input_info('1984', '2021', 'АСТ', 'Научная фантастика', 'Джордж Оруэлл', '214₽')
b1.print_book_info()
b1.set_name('Дни в Бирме')
b1.get_name()

