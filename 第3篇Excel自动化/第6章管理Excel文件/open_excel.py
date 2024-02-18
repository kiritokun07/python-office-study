import os

import xlwings as xw

if __name__ == '__main__':
    path = 'excel'
    files = os.listdir(path)
    print(files)
    # 注意如果这里是不可见，那么没有quit的话就会常驻后台
    app = xw.App(visible=True, add_book=False)
    for file in files:
        app.books.open(f'{path}{os.sep}{file}')
    # with xw.App(visible=True, add_book=False) as app:
    #     app.books.open('excel/上海-区域表.xlsx')
