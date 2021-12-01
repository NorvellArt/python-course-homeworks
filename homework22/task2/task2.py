with open('task1.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
        print(line.strip())
        print(f' {len(line)} симв. {len(line.split())} сл.')
print(count, 'стр.')
