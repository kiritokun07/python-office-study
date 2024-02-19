import xlwings as xw

if __name__ == '__main__':
    nameFile = 'excel\\数据区域.xlsx'
    with xw.App(visible=False, add_book=False) as app:
        app.display_alerts = False
        workbook: xw.Book = app.books.open(nameFile)
        sheetCount = len(workbook.sheets)
        print(f'该文件中有{sheetCount}个工作表')

        sheet0: xw.Sheet = workbook.sheets[0]
        sheet0UsedRange: xw.Range = sheet0.used_range
        print(f'工作表有效区域是：{sheet0UsedRange}，'
              f'该工作表一共有{sheet0UsedRange.last_cell.row}行，{sheet0UsedRange.last_cell.column}列')

        # 将行数和列数转换为行标和列标
        last_cell = chr(64 + sheet0UsedRange.last_cell.column) + str(sheet0UsedRange.last_cell.row)
        print(f'数据区域的最后一个单元格是{last_cell}')

        workbook.close()
