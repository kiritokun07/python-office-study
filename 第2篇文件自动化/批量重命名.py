import os

if __name__ == '__main__':
    oldPathName = '哈哈哈'
    newPathName = '批量文件夹'
    for i, dirName in enumerate(os.listdir(oldPathName)):
        newDirName = dirName[2:]
        # newDirName = '哈哈' + dirName
        print(f'重命名:{dirName}为:{newDirName}')
        os.rename(oldPathName + os.sep + dirName, oldPathName + os.sep + newDirName)

    print(f'重命名父文件夹:{oldPathName} 为:{newPathName}')
    os.rename(oldPathName, newPathName)
