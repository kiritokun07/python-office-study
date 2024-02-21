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

            # 查看调整前的行高和列宽
            a1_height, a1_width = myutils.get_row_height_and_column_width(worksheet.range('A1'))
            print(f'单元格A1原来的行高和列宽分别是 {a1_height} {a1_width}')

            # 设置表头自动调整行高和列宽
            worksheet.range('A1').expand('right').autofit()

            a1_height, a1_width = myutils.get_row_height_and_column_width(worksheet.range('A1'))
            print(f'自动调整后 单元格A1的行高和列宽分别是 {a1_height} {a1_width}')

            # 手动设置行高
            worksheet.range('A1').expand('right').row_height = 55

            a1_height, a1_width = myutils.get_row_height_and_column_width(worksheet.range('A1'))
            print(f'手动调整后 单元格A1的行高和列宽分别是 {a1_height} {a1_width}')

            workbook.save()
            workbook.close()
