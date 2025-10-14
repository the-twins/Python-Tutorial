if __name__ == '__main__':
    with open('hello.txt', 'a', encoding="utf-8") as f:
        f.write('Hello world!\n')
    with open('hello.txt', 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
