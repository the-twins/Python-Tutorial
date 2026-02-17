if __name__ == '__main__':
    n = 1
    with open('hello.txt', 'r') as f:
        for i in f:
            print(n, i)
            n += 1
        f.seek(0)
        for i in f:
            print(i)