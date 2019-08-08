import os
dir = os.getcwd()

filename = rf"{dir}\peening.txt"


file = open(filename)
txt = file.readlines()
file.close

zb = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
zb_temp = {}

import skip, extract

for line in txt:
    is_skip, strr = skip.skip(line)

    if is_skip:
        continue
    else:
        zb_temp = extract.extract(strr)

    for i in range(1,6):
        if zb_temp[i] != -9999.0:
            zb[i] = zb_temp[i]  #zb is a list with 5 floats
    print(zb)




def rotation_matrix():
    pass

def catia_operation():
    pass
