import csv

with open('data2.csv') as f:
    reader = csv.reader(f, lineterminator=',')
    for item in reader:
        new_item = item.pop(0).split(';')
        print(new_item)
