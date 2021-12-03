import os.path

lst = []
for root, dirs, files in os.walk('files', topdown=True):
    for name in files:
        lst.append(os.path.join(root, name))
    for name in dirs:
        lst.append(os.path.join(root, name))

print(lst)
