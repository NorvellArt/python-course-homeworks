import re

emails = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
reg = r"[\w.%+-]+@[\w.-]+\.[a-z]{2,}\b"
print(re.findall(reg, emails))
