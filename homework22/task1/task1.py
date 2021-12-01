file1 = 'file1.txt'
file2 = 'file2.txt'
file3 = 'file3.txt'

with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(file3, 'w', encoding='utf-8') as f3:
    f3.write(f'Третий файл = {f1.read()}{f2.read()}')
