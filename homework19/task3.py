import re


def is_telephone_number(num):
    pattern = r'^(\+?7) ?((\(\d{3}\))|(\d{3}))?( )?(\d{3}[\- ]?\d{2}[\- ]?\d{2})( +)?$'
    if re.search(pattern, num):
        return True
    return False


print(is_telephone_number('+7 499 456-45-78'))
print(is_telephone_number('+74994564578'))
print(is_telephone_number('7 (499) 456 45 78'))
print(is_telephone_number('7 (499) 456-45-78'))
print(is_telephone_number('7 (499) 45-45-7'))
print(is_telephone_number('499 456-45-78'))
print(is_telephone_number('6-45-78'))
print(is_telephone_number('7 (499)-4564578'))
