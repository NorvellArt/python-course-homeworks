import os.path

lst = []
for root, dirs, files in os.walk('Work', topdown=True):
    for name in files:
        lst.append(os.path.join(root, name))

for path in lst:
    if os.path.getsize(path) != 0:
        print(f'{path} - {os.path.getsize(path)} bytes')

os.mkdir('Work/empty_files')
print('-' * 50)

for path in lst:
    if os.path.getsize(path) == 0:
        print(f'Файл {os.path.basename(path)}, из папки {os.path.dirname(path)}, перемещен в папку Work\\empty_files')
        os.renames(path, f'Work/empty_files/{os.path.basename(path)}')
