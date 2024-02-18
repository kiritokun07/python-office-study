import xlwings as xw

if __name__ == '__main__':
    src_name = 'excel\\源表.xlsx'
    delete_sheet_name = '地址'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        src_workbook = app.books.open(src_name)
        src_worksheets = src_workbook.sheets

        for sheet in src_worksheets:
            if sheet.name == delete_sheet_name:
                print(f'删除文件 {src_name} 中的 {delete_sheet_name} 表')
                sheet.delete()
        src_workbook.save()
        src_workbook.close()
