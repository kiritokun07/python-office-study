import xlwings as xw


# 是否是临时文件名 以 ~$ 开头
def is_temp_file(file: str) -> bool:
    return file.startswith('~$')


# 是否是xlsx文件
def is_xlsx(file: str) -> bool:
    return file.endswith('.xlsx')


# 获取工作表已使用最大的行数
def last_row(sheet: xw.Sheet) -> int:
    sheet_used_range: xw.Range = sheet.used_range
    return sheet_used_range.last_cell.row


# excel 列数转列标
def num_to_excel_column(num: int) -> str:
    result = ''
    while num > 0:
        num, remainder = divmod(num - 1, 26)
        letter = chr(65 + remainder)
        result = letter + result
    return result or 'A'
