import xlwings as xw

if __name__ == '__main__':
    nameFile = 'excel\\指定工作表.xlsx'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook: xw.Book = app.books.open(nameFile)
        sheetCount = len(workbook.sheets)
        print(f'该文件中有{sheetCount}个工作表')

        worksheet: xw.Sheet = workbook.sheets['Sheet10']

        # 如果数据在一列，会返回一维数组，用.expand('down')读也是一样
        # a1_value = worksheet.range('A2:A4').value
        a1_value = worksheet.range('A1').expand().value
        print(a1_value)
        workbook.close()
