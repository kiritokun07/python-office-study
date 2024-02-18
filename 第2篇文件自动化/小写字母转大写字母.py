if __name__ == '__main__':
    data = []
    with open('小写字母.txt', 'r') as f:
        for line in f:
            data.append(line)
    print(data)

    with open('转换后的大写字母.txt', 'w') as f_write:
        for line in data:
            f_write.write(line.upper())
