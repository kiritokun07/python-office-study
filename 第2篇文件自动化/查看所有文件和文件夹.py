import os

if __name__ == '__main__':
    pwd = os.getcwd()
    print(f'当前路径是：{pwd}')
    allFiles = os.listdir(pwd)
    print(allFiles)
    allFiles2 = os.listdir('data/')
    print(allFiles2)
