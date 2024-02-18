import xlwings as xw

if __name__ == '__main__':
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.add()
    worksheet = workbook.sheets['Sheet1']
    range_a1 = worksheet.range('B3')
    range_a1.value = '地区'
    print(f'行高是 {range_a1.row_height}，列宽是 {range_a1.column_width}')
    print(f'单元格颜色是：{range_a1.color}')
    range_a1.row_height = 20
    range_a1.column_width = 10
    print(f'新行高是 {range_a1.row_height}，列宽是 {range_a1.column_width}')
    range_a1.color = (50, 130, 20)
    print(f'新单元格颜色是：{range_a1.color}')
    print(range_a1.address)
    print(range_a1.row, range_a1.column)
    print(range_a1.current_region)
