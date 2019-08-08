import sys





def skip(txt):
    str_temp = txt.strip().upper()

    l_paren = str_temp.count("(")
    r_paren = str_temp.count(")")

    if l_paren != r_paren or l_paren > 2 or r_paren > 2 :
        print("小括号数量不对,请检查：")
        print(str_temp)
        sys.exit()

    while l_paren > 0:
        l_str = str_temp[0 : str_temp.find('(')]
        r_str = str_temp[str_temp.find(')') + 1 : ]
        str_temp = l_str + r_str
        l_paren = str_temp.count("(")

    str = str_temp

    str = str.strip()

    #print(str)

    if str == '':
        return True, str

    if 'G4' in str or 'G04' in str:
        return True, str

    openair = ['IF',
        'M03', 'M04',
        'M51', 'M52',
        'M61', 'M71']

    for i in openair:
        if i in str:
            return True, str

    if str[0] != 'N':
        return True, str

    zuobiao = ['X', 'Y', 'Z', 'A', 'B']
    for i in zuobiao:
        if i in str:
            return False, str



    return True, str
