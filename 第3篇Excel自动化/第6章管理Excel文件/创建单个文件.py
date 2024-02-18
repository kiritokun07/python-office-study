import xlwings as xw

if __name__ == '__main__':
    # 第一步 打开 Excel 软件
    app = xw.App(visible=False, add_book=False)
    # 第二步 创建工作簿并保存
    workbook = app.books.add()

    # 用 save 方法保存 Excel 文件
    workbook.save('excel\\output.xlsx')

    # 第三步 关闭工作簿并退出 Excel 程序
    workbook.close()
    app.quit()
