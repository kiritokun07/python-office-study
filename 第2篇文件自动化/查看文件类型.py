import os

if __name__ == '__main__':
    allFiles = os.listdir('data')
    for i in allFiles:
        fileName = os.path.splitext(i)[0]
        fileType = os.path.splitext(i)[1]
        print(f'文件{fileName}的类型是{fileType}')
