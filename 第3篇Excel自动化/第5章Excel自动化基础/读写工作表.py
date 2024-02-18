import xlwings as xw

if __name__ == '__main__':
    app = xw.App(visible=True, add_book=False)
    # 新建一个工作簿 同时默认创建了 Sheet1 工作表
    workbook = app.books.add()
    print(workbook.name)
    # 选中工作表 Sheet1
    worksheet: xw.Sheet = workbook.sheets['Sheet1']
    print(worksheet.name)
    worksheet.range('A1').value = '地区'
    value = worksheet.range('A1').value
    print(value)
