def uppercase(str):
    for i in str:
        str = chr(ord(i) - 32)
        print('{}'.format(str), end='')
