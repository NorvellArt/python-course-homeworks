import re

password = 'my-p@ssw0rd'
reg = r'^[a-z0-9@_-]{6,18}$'
print(re.findall(reg, password, re.I))
