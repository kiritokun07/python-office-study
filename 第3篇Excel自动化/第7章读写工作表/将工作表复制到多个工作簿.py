import os

import xlwings as xw

if __name__ == '__main__':
    srcFile = 'excel' + os.sep + '源工作表.xlsx'
    newSheetName = '汇总数据'
    destFile = 'excel' + os.sep + '汇总表.xlsx'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        srcWorkbook: xw.Book = app.books.open(srcFile)
        sheetCount = len(srcWorkbook.sheets)
        print(f'该文件中有{sheetCount}个工作表')
        srcWorkSheet: xw.Sheet = srcWorkbook.sheets[0]
        print(srcWorkSheet.name)
        srcSheetValue = srcWorkSheet.range('A1').expand().value

        # 给已有Excel加一个工作表
        destBook: xw.Book = app.books.open(destFile)
        destSheet: xw.Sheet = destBook.sheets.add(newSheetName)
        # 这里就复制了内容没有复制格式，也没有公式
        destSheet.range('A1').value = srcSheetValue
        destBook.save()
        destBook.close()

        srcWorkbook.close()
