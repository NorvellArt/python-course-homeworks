def opener():
    f = open('text.txt', 'w')
    f.write('This is text line number 1;\nThis is text line number 2;\nThis is text line number 3;\n')
    f.close()
    f = open('text.txt', 'r')
    print(f.read())
    f.close()


def closer(lst):
    f = open('text.txt', 'w')
    f.writelines(lst)
    f.close()
    f = open('text.txt', 'r')
    print(f.read())
    f.close()