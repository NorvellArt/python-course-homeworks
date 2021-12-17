class TemperatureConverter:
    __count = 0

    @staticmethod
    def celsius_to_fahrenheit(x):
        if isinstance(x, (int, float)):
            TemperatureConverter.__count += 1
            return (x * 1.8) + 32
        else:
            raise ValueError('Температура должна быть числом')

    @staticmethod
    def fahrenheit_to_celsius(x):
        if isinstance(x, (int, float)):
            TemperatureConverter.__count += 1
            return (x - 32) / 1.8
        else:
            raise ValueError('Температура должна быть числом')

    @staticmethod
    def get_temp_count():
        return TemperatureConverter.__count


print(TemperatureConverter.celsius_to_fahrenheit(15))
print(TemperatureConverter.fahrenheit_to_celsius(59))
print(TemperatureConverter.celsius_to_fahrenheit(30))
print(TemperatureConverter.fahrenheit_to_celsius(86))
print('Количество подсчетов:', TemperatureConverter.get_temp_count())
