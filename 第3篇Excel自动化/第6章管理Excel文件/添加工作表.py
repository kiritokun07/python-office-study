import xlwings as xw

if __name__ == '__main__':
    with xw.App(visible=False, add_book=False) as app:
        # 关闭告警信息（关闭前提示保存、删除前提示确认）
        app.display_alerts = False
        workbook: xw.Book = app.books.open('excel/output.xlsx')
        print(f'当前活跃工作表是：{workbook.sheets.active}')
        # 如果不指定 before after 那么默认创建的工作表在active的表之前
        worksheet: xw.Sheet = workbook.sheets.add('test2')
        print(f'添加表后当前活跃工作表是：{workbook.sheets.active}')
        workbook.save()
        workbook.close()
