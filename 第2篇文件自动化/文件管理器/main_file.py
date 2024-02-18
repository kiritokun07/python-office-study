import os

import file_all_op as fo

if __name__ == '__main__':
    path = r'..\data'
    os.chdir(path)
    files = os.listdir(path)
    print('所有的文件：\n', files)
    fo.show_command()
    file_op = int(input('请输入指令：'))
    if file_op == 1:
        '''模糊查找文件'''
        fo.find_files(files)
    elif file_op == 2:
        '''删除文件'''
        fo.del_files(files)
    elif file_op == 3:
        '''重命名文件'''
        fo.rename_files(files)
    else:
        print('请输入正确的指令!')
