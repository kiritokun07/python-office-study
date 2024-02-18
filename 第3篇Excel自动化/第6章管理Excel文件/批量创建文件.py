import xlwings as xw

if __name__ == '__main__':
    prefixName = ['北京', '上海', '天津', '广州', '武汉', '广东', '河北']

    # 第一步 打开 Excel 软件
    with xw.App(visible=False, add_book=False) as app:
        # 用 for 循环创建多个文件
        for prefix in prefixName:
            print(f'正在创建 {prefix} 区域的Excel文件')
            # 第二步 创建工作簿并保存
            with app.books.add() as workbook:
                workbook.save(f'excel\\{prefix}-区域表.xlsx')
            print(f'创建 {prefix} 文件成功')
    print('批量创建成功！')
