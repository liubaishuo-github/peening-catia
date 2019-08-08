def extract(str_temp):

    l_paren = str_temp.count("[")
    r_paren = str_temp.count("]")

    if l_paren != r_paren:
        print("方括号数量不对,请检查：")
        print(str_temp)
        sys.exit()

    strr = str_temp

    if 'F' in str_temp:
        strr = str_temp[0 : str_temp.find('F')]


    l_paren = strr.count("[")

    while l_paren != 0:
        r_cal = strr[strr.find('[') + 1 : strr.find(']')]
        val = eval(r_cal)
        val_str = str(val)

        strr = '{}{}{}'.format(strr[0 : strr.find('[')], val_str,
                                strr[strr.find(']') + 1 : ])

        l_paren = strr.count("[")


    print(strr)

    sl = [1,2,3,4,5]

    position = {}
    position[1] = strr.find('X')
    position[2] = strr.find('Y')
    position[3] = strr.find('Z')
    position[4] = strr.find('A')
    position[5] = strr.find('B')

    import copy

    position_temp = copy.deepcopy(position)

    for i in range(1, 6):
        minn = position_temp[i]
        jj = i

        for j in range(i+1, 6):
            if minn > position_temp[j]:
                minn = position_temp[j]
                jj = j

        sl[jj-1] , sl[i-1] = sl[i-1], sl[jj-1]
        position_temp[i], position_temp[jj] = position_temp[jj], position_temp[i]

    sl.append(-1)

    #print(sl)
    #print(position)
    zb_str = {1: '-9999', 2: '-9999', 3: '-9999', 4:'-9999', 5:'-9999'}

    for i in range(0,5):
        if position[sl[i]] == -1:
            #print('sl:', sl[i])
            #print(position[sl[i]])
            continue
        elif sl[i+1] != -1:
            #print('sl:', sl[i])
            #print(position[sl[i]])
            zb_str[sl[i]] = strr[position[sl[i]] + 1 : position[sl[i+1]]]
        elif sl[i+1] == -1:
            #print('sl:', sl[i])
            #print(position[sl[i]])
            zb_str[sl[i]] = strr[position[sl[i]] + 1 : ]

    #print(zb_str)
    zb_val ={}
    for i in range(1,6):
        zb_val[i] = float(zb_str[i])

    #print(zb_val)
    return zb_val
