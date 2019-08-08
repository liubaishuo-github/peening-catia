import win32com.client
CATIA = win32com.client.Dispatch('catia.application')
oPart = CATIA.ActiveDocument.part
#myHBody = oPart.HybridBodies.Add()
#referencebody = oPart.CreateReferenceFromObject(myHBody)
#oPart.HybridShapeFactory.ChangeFeatureName(referencebody, "GeometryFromExcel")

myPBody = oPart.HybridBodies.Item("point")
Point = oPart.HybridShapeFactory.\
                        AddNewPointCoord(1, 2, 3)
#myPBody.AppendHybridShape(Point)

Dir = oPart.HybridShapeFactory.\
            AddNewDirectionByCoord(1, -1, 4)


Line = oPart.HybridShapeFactory.\
           AddNewLinePtDir(Point, Dir, 0, 300, False)

myPBody.AppendHybridShape(Line)

ref_line = oPart.CreateReferenceFromObject(Line)
oPart.HybridShapeFactory.ChangeFeatureName(ref_line, "haha")


oPart.Update()
