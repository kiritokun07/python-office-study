import matplotlib.pyplot as plt
import xlwings as xw

if __name__ == '__main__':
    app = xw.App(visible=True, add_book=False)
    workbook = app.books.add()
    worksheet = workbook.sheets['Sheet1']
    worksheet.range('A1').value = [1, 2, 3, 4, 6, 7, 9]
    # 获取表格中的所有数据
    value_a1 = worksheet.range('A1').expand('table').value
    print(value_a1)
    # 获取画布
    fig = plt.figure()
    plt.plot(value_a1)
    # 把图写入 Excel 文件中
    worksheet.pictures.add(fig, name='test_plot', left=300, top=20)
