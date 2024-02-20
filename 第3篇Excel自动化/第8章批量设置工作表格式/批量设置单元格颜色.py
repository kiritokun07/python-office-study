import os

import xlwings as xw

import myutils

if __name__ == '__main__':
    destPath = 'excel\\group'
    destFiles = os.listdir(destPath)
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        for file in destFiles:
            print('-----------------')
            if myutils.is_temp_file(file):
                continue
            if not myutils.is_xlsx(file):
                continue
            if file.startswith('颜色'):
                continue
            print(f'正在处理文件 {file}')
            workbook: xw.Book = app.books.open(destPath + os.sep + file)
            worksheet: xw.Sheet = workbook.sheets[0]
            headColor = worksheet.range('A1').expand('right').color
            print(f'原来的表头颜色是 {headColor}')
            worksheet.range('A1').expand('right').color = (205, 38, 38)
            headColor = worksheet.range('A1').expand('right').color
            print(f'设置后表头颜色是 {headColor}')
            lastRow = myutils.last_row(worksheet)
            print(f'lastRow={lastRow}')
            # 是否是奇数 True 奇数 False 不是奇数
            isOdd: bool = False
            for i in range(2, lastRow + 1):
                if isOdd:
                    color_i = worksheet.range(f'A{i}').expand('right').color
                    print(f'第{i}行原来的颜色是 {color_i}')
                    worksheet.range(f'A{i}').expand('right').color = (30, 144, 255)
                    color_i = worksheet.range(f'A{i}').expand('right').color
                    print(f'设置后第{i}行新的颜色是 {color_i}')
                # 最后一定要反转bool值
                isOdd = not isOdd
            workbook.save('excel\\group\\颜色-' + file)
            workbook.close()
