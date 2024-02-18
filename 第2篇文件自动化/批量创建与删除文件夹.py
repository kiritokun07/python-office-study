import os.path

if __name__ == '__main__':
    dir_name = '批量文件夹'
    dir_num = 20


    def get_path_name(i: int):
        return f'{dir_name}\第{i + 1}个数据'


    if os.path.exists(dir_name):
        for i in range(dir_num):
            path_name = get_path_name(i)
            print(f'删除文件夹{path_name}')
            os.removedirs(path_name)
    else:
        os.mkdir(dir_name)
        for i in range(dir_num):
            path_name = get_path_name(i)
            print(f'创建文件夹{path_name}')
            os.makedirs(path_name)
        print(os.listdir(dir_name))
