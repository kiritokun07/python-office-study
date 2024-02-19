import xlwings as xw

if __name__ == '__main__':
    nameFile = 'excel\\要删除数据的表格.xlsx'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook: xw.Book = app.books.open(nameFile)
        sheetCount = len(workbook.sheets)
        print(f'该文件中有{sheetCount}个工作表')

        worksheet: xw.Sheet = workbook.sheets[0]
        # 删除数据及格式
        # worksheet.range('A1').clear()
        # worksheet.range('C1').clear_contents()
        # worksheet.range('B2').clear_contents()
        #
        # worksheet.range('A1').value = 'AAAA'
        # worksheet.range('C1').value = 'CCCC'

        # 删除单元格区域的数据0
        # worksheet.range('A1').expand().clear_contents()

        # 删除全部数据
        worksheet.clear_contents()
        workbook.save('temp.xlsx')
        workbook.close()
