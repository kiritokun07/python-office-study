import xlwings as xw

if __name__ == '__main__':
    with xw.App(visible=False, add_book=False) as app:
        # 关闭告警信息（关闭前提示保存、删除前提示确认）
        app.display_alerts = False
        workbook = app.books.open('excel/output.xlsx')
        workbook.sheets.add()
        print(f'当前活跃工作表是：{workbook.sheets.active}')
        workbook.save()
        workbook.close()
