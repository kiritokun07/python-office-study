import xlwings as xw

if __name__ == '__main__':
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.add()
    worksheet = workbook.sheets['Sheet1']
    worksheet.range('A1').value = [1, 2, 3, 4, 6, 7, 9]
    # 写入公式
    cellH1 = worksheet.range('H1')
    cellH1.formula = '=SUM(A1:G1)'
    print(f'公式是 {cellH1.formula_array}')
    print(f'公式是 {cellH1.formula}')
