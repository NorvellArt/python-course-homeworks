import re

text = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежеиесячных осадков.'
reg = r'(?:\d{2}/){2}(?:\d{4})'
print(re.findall(reg, text))

