import xlwings as xw

# def init_excel():
#     xw.Book


if __name__ == '__main__':
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook = app.books.open('excel\\写单元格表.xlsx')
        worksheet = workbook.sheets['表1']

        # 写单元格
        values = [['产品', '数目', '单价'], ['计算机类图书', '100', '99.98']]
        worksheet.range('A1').value = values
        # worksheet.range('A1').value = '产品'
        # worksheet.range('A2').value = '计算机类图书'
        # worksheet.range('B1').value = '数目'
        # worksheet.range('B2').value = '100'
        # worksheet.range('C1').value = '单价'
        # worksheet.range('C2').value = '99.98'
        workbook.save()
        workbook.close()
