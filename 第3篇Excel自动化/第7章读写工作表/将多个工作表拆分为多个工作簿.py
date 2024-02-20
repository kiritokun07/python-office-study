import os

import xlwings as xw

if __name__ == '__main__':
    nameFile = 'excel' + os.sep + '合并工作表.xlsx'
    # newSheetName = '各组汇总数据'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook: xw.Book = app.books.open(nameFile)
        allSheets = workbook.sheets
        print(f'该文件中有{len(allSheets)}个工作表')
        for sheet in allSheets:
            with app.books.add() as newBook:
                # 第一种方式 复制工作表的内容
                # newSheet: xw.Sheet = newBook.sheets.add(sheet.name)
                # newSheet.range('A1').value = sheet.range('A1').expand().value
                # 第二种方式 直接copy工作表 此时会将格式、公式复制过来
                sheetI: xw.Sheet = sheet
                sheetI.copy(before=newBook.sheets[-1])
                newBook.save(f'excel\\合并工作表拆分-{sheet.name}.xlsx')
        workbook.close()
