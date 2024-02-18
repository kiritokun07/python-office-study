import os


def show_command():
    """
    提示用户输入的指令
    :return:
    """
    print('----------------')
    print('请输入不同的指令')
    print('1 模糊查找文件')
    print('2 删除文件')
    print('3 重命名文件')
    print('----------------')


def find_files(files: list[str]):
    """模糊查找文件"""
    file_file = input('请输入要模糊查找的文件名：')
    end_file = input('请输入文件类型：')
    for file in files:
        if file.endswith(end_file) and file_file in file:
            print(f'找到文件名包括"{file_file}"并且文件类型是"{end_file}"的文件->{file}')


def del_files(files: list[str]):
    """删除文件"""
    del_file = input('请输入需要删除的文件名：')
    if del_file in files:
        print(f'您将删除文件 {del_file}')
        confirm = input('请再次确认是否删除（Y/N）：')
        if confirm == 'Y' or confirm == 'y':
            os.remove(del_file)
            print(f'您已经删除 {del_file}')
        else:
            print('取消删除')
    else:
        print(f'文件 {del_file} 不存在，无法删除！')


def rename_files(files: list[str]):
    """重命名文件"""
    rename_file = input('请输入需要重命名的文件名：')
    if rename_file not in files:
        print(f'文件 {rename_file} 不存在，无法重命名')
        return
    else:
        new_name_file = input('请输入新的文件名：')
        print(f'文件 {rename_file} 存在，将重命名为 {new_name_file}')
        os.rename(rename_file, new_name_file)
