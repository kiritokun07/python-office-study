import os

import xlwings as xw

if __name__ == '__main__':
    nameFile = 'excel' + os.sep + '合并工作表.xlsx'
    newSheetName = '各组汇总数据'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook: xw.Book = app.books.open(nameFile)
        print(f'该文件中有{len(workbook.sheets)}个工作表')

        newSheet: xw.Sheet = workbook.sheets.add(newSheetName, before=workbook.sheets[0].name)
        print(f'添加 {newSheetName} 工作表后该文件中有{len(workbook.sheets)}个工作表')

        header = None

        mySheet: xw.Sheet
        print('开始合并！')
        print('------------------')
        for sheetI in workbook.sheets:
            mySheet = sheetI
            print(f'当前工作表的名字是：{mySheet.name}')
            print('开始合并该工作表')
            if mySheet.name == newSheetName:
                print('该工作表不需要合并')
                continue
            sheetAllData = mySheet.range('A2').expand().value
            if header is None:
                header = mySheet.range('A1').expand('right').value
                print('首先写入表头')
                newSheet.range('A1').value = header
            print(f'开始吧工作表 {mySheet.name} 的所有数据写入汇总后的工作表 {newSheetName}')

            usedRange: xw.Range = newSheet.used_range
            lastRow = usedRange.last_cell.row
            print(f'当前最后一行是：{lastRow}')
            newSheet.range(f'A{lastRow + 1}').value = sheetAllData
            print(f'合并工作表 {mySheet.name} 完成！')
            print('------------------')

        workbook.save('excel\\合并工作表2.xlsx')
        print('保存汇总后的工作表到 合并工作表2.xlsx')
        workbook.close()
