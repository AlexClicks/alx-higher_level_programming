def read_file(Text.txt):
    with open(Text, 'r', encoding='utf8') as f:
        for line in f:
            print(line, end='')

