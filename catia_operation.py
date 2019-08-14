import win32com.client

def cat_op(x, y, z, di, dj, dk, name, myPBody, oPart):


    '''
    CATIA = win32com.client.Dispatch('catia.application')
    oPart = CATIA.ActiveDocument.part
    myPBody = oPart.HybridBodies.Add()
    ref_body = oPart.CreateReferenceFromObject(myPBody)
    oPart.HybridShapeFactory.ChangeFeatureName(ref_body, "GeometryFromNC")
    '''

    #CATIA = win32com.client.Dispatch('catia.application')
    #oPart = CATIA.ActiveDocument.part

    #myPBody = oPart.HybridBodies.Item("GeometryFromNC")
    Point = oPart.HybridShapeFactory.\
                    AddNewPointCoord(x * 25.4, y * 25.4, z * 25.4)

    Dir = oPart.HybridShapeFactory.\
                AddNewDirectionByCoord(di, dj, dk)


    Line = oPart.HybridShapeFactory.\
               AddNewLinePtDir(Point, Dir, 0, 6 * 25.4, False)

    myPBody.AppendHybridShape(Line)

    ref_line = oPart.CreateReferenceFromObject(Line)
    oPart.HybridShapeFactory.ChangeFeatureName(ref_line, name)


    oPart.Update()
