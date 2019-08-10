import os
dir = os.getcwd()

filename = rf"{dir}\peening.txt"


file = open(filename)
txt = file.readlines()
file.close

zb = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
zb_temp = {}

import skip, extract, rotation_matrix, catia_operation, win32com.client


CATIA = win32com.client.Dispatch('catia.application')
oPart = CATIA.ActiveDocument.part
myPBody = oPart.HybridBodies.Add()
ref_body = oPart.CreateReferenceFromObject(myPBody)
oPart.HybridShapeFactory.ChangeFeatureName(ref_body, "GeometryFromNC")


for line in txt:
    is_skip, strr = skip.skip(line)

    if is_skip:
        continue
    else:
        zb_temp, name = extract.extract(strr)

    #print(type(zb_temp))
    #print(type(name))

    for i in range(1,6):
        if zb_temp[i] != -9999.0:
            zb[i] = zb_temp[i]  #zb is a list or dict? with 5 floats
    #print(type(zb))
    #print(zb)
    #print(zb)
    catia_operation.cat_op(*rotation_matrix.transf(*zb.values()), \
                            name, myPBody, oPart)
