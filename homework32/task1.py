class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Секунды должны быть целым числом')

        self.__secs = secs % self.__DAY

    def __eq__(self, other):
        return self.__secs == other.__secs

    def __gt__(self, other):
        return self.__secs > other.__secs

    def __ge__(self, other):
        return self.__secs >= other.__secs

    def __lt__(self, other):
        return self.__secs < other.__secs

    def __le__(self, other):
        return self.__secs <= other.__secs


c1 = Clock(300)
c2 = Clock(600)
print(f'c2 > c1 {c2 > c1}')
print(f'c2 >= c1 {c2 >= c1}')
print(f'c2 < c1 {c2 < c1}')
print(f'c2 <= c1 {c2 <= c1}')
