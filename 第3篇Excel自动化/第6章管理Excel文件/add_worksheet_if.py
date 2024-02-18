import xlwings as xw

if __name__ == '__main__':
    excel_name = 'excel/output.xlsx'
    new_sheet = '姓名3'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook = app.books.open(excel_name)
        all_sheet_name = [sheet.name for sheet in workbook.sheets]
        print(all_sheet_name)

        # 这里需要在判断中忽略大小写，因为Excel的Sheet中大小写被忽视了
        if new_sheet in all_sheet_name:
            print(f'文件已存在sheet {new_sheet}')
        else:
            workbook.sheets.add(new_sheet)
            print(f'当前活跃工作表是：{workbook.sheets.active}')
        workbook.save()
        workbook.close()
