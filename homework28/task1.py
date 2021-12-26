class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, value):
        self.__percent = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):
        self.surname = surname

    def add_money(self, value):
        self.value += value
        print(f'Вы внесли {value} {Account.suffix}')
        self.print_balance()

    def add_percents(self):
        self.value += self.value * self.percent
        print('Проценты успешно начислены!')
        self.print_balance()

    def withdraw_money(self, value):
        if value > self.value:
            print(f'Недостаточно средств.')
        else:
            self.value -= value
            print(f'{value} {Account.suffix} было успешно снято.')
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):
        euro_val = Account.convert(self.value, Account.rate_euro)
        print(f'Состояние счета: {euro_val} {Account.suffix_eur}.')

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}.')

    def print_info(self):
        print('Информация о счете')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)


acc = Account('Иванов', 12345, 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
acc.edit_owner('Дюма')
acc.print_info()
print()
acc.add_percents()
print()
acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
