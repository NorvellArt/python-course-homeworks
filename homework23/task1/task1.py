import os.path

path = r'test_dir/f1/4.txt'

if os.path.exists(path):
    print(f'{os.path.basename(path)} ({os.path.dirname(path)}) - last access time {os.path.getatime(path)} sec')
else:
    print('Такого файла не существует')
