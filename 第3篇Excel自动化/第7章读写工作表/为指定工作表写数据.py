import xlwings as xw

if __name__ == '__main__':
    nameFile = 'excel\\指定工作表.xlsx'
    rowData = [['种类', '数目', '单价', '销售平台'],
               ['Python', 100, 99.98, '当当'],
               ['Java', 130, 98.98, '京东'],
               ['C++', 90, 79.98, '京东']]
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook: xw.Book = app.books.open(nameFile)
        sheetCount = len(workbook.sheets)
        print(f'该文件中有{sheetCount}个工作表')

        sheet7: xw.Sheet = workbook.sheets[7]
        print(sheet7.name)  # 打印 Sheet8
        sheet7.range('A1').value = rowData
        sheet3: xw.Sheet = workbook.sheets['Sheet10']
        sheet3.range('A1').value = rowData

        workbook.save()
        workbook.close()
