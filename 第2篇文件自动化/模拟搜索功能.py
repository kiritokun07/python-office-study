import os

if __name__ == '__main__':
    needFind = 'test'
    pathName = 'data'
    allFiles: list[str] = []
    for root, dirs, files in os.walk(pathName):
        for file in files:
            allFiles.append(file)
    print(allFiles)

    for file in allFiles:
        if needFind in file:
            print('找到了->', file)
