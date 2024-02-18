if __name__ == '__main__':
    try:
        print(1 / 0)
    except Exception as e:
        print('异常：', e)
    finally:
        print('finally')
