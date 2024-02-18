import os

if __name__ == '__main__':
    pathName = 'data'
    for root, dirNames, filenames in os.walk(pathName):
        print(f'当前目录：{root}')
        print(f'它的子文件夹列表：{dirNames}')
        print(f'它包含的文件列表：{filenames}')
