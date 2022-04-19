import os, RLPy, math
from winreg import *
import os

def UpdateProp(prop, x, y, rotationValue):

    #-- Get Transform Control and Data --#
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

    #-- Time 2s set X transform Key to 300 --#
    ts_data_block.SetData("Position/PositionX", RLPy.RTime(0), RLPy.RVariant(x * 1000))

    if (rotationValue < 0):
        #-- Set Rotation Z 
        ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(0), RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))

    if (y > 0):
        
        #-- Set Rotation Y
        ts_data_block.SetData("Position/PositionY", RLPy.RTime(0), RLPy.RVariant((y * 1000) * -1))

Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
RawKey = OpenKey(Registry, r"SOFTWARE\Reallusion\iClone\7.0")
ic_template_path = os.path.abspath(QueryValueEx(RawKey, "Template Data" )[0])

# Load Box_001.iProp
RLPy.RFileIO.LoadFile("C:\\Users\\Public\\Documents\\Reallusion\\Template\\iClone 7 Template\\iClone Template\\Props\\City Elements\Floors\\Road\\B064C_Road-01.iProp")

propName = "Road-01"
prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, propName)
prop.SetName("Road")

for x in range(1, 10):
    prop2 = prop.Clone()
    prop2.SetName("Road" + str(x + 1))    
    UpdateProp(prop2, x, 0, 0)

for x in range(1, 10):
    prop2 = prop.Clone()
    prop2.SetName("Road" + str(x + 10))
    UpdateProp(prop2, 10, x, -90)

for x in range(1, 11):
    prop2 = prop.Clone()
    prop2.SetName("Road" + str(x + 20))
    UpdateProp(prop2, x -1, 10, -180)

for x in range(1, 10):
    prop2 = prop.Clone()
    prop2.SetName("Road" + str(x + 30))
    UpdateProp(prop2, -1, x, -270)

# Load B064C_Road-05.iProp
RLPy.RFileIO.LoadFile("C:\\Users\\Public\\Documents\\Reallusion\\Template\\iClone 7 Template\\iClone Template\\Props\\City Elements\Floors\\Road\\B064C_Road-05.iProp")

propName = "Road-05"
cornerProp = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, propName)
cornerProp.SetName("Corner1Road")
UpdateProp(cornerProp, -1, 0, 0)

cornerProp2 = cornerProp.Clone()
cornerProp2.SetName("Corner2Road")
UpdateProp(cornerProp2, 10, 0, -90)

cornerProp3 = cornerProp.Clone()
cornerProp3.SetName("Corner3Road")
UpdateProp(cornerProp3, 10, 10, -180)

cornerProp4 = cornerProp.Clone()
cornerProp4.SetName("Corner4Road")
UpdateProp(cornerProp4, -1, 10, -270)

# SUV White
RLPy.RFileIO.LoadFile("C:\\Users\\Public\\Documents\\Reallusion\\Template\\iClone 7 Template\\iClone Template\\Props\\Interactive Vehicles Series\\SUV\\SUV White.iProp")

suv = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "SUV_White")  

#-- Get Transform Control and Data --#
ts_control = suv.GetControl("Transform")
ts_data_block = ts_control.GetDataBlock()

#-- Move into inside lane --#
ts_data_block.SetData("Position/PositionY", RLPy.RTime(0), RLPy.RVariant(-150))

#-- Move to the end of the road --#
ts_data_block.SetData("Position/PositionX", RLPy.RTime(10000), RLPy.RVariant(9200))

#-- Turn Right --#
rotationValue = -90
ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(9940), RLPy.RVariant(0))
ts_data_block.SetData("Position/PositionY", RLPy.RTime(9940), RLPy.RVariant(-150))
ts_data_block.SetData("Position/PositionX", RLPy.RTime(10800), RLPy.RVariant(9840))
ts_data_block.SetData("Position/PositionY", RLPy.RTime(10800), RLPy.RVariant(-768))
ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(10800), RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))
ts_data_block.SetData("Position/PositionY", RLPy.RTime(20000), RLPy.RVariant(-9200))

#-- Turn Right Again--#
rotationValue = -180
ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(19940), RLPy.RVariant(0))
ts_data_block.SetData("Position/PositionY", RLPy.RTime(19940), RLPy.RVariant(-150))
ts_data_block.SetData("Position/PositionX", RLPy.RTime(20800), RLPy.RVariant(9840))
ts_data_block.SetData("Position/PositionY", RLPy.RTime(20800), RLPy.RVariant(-768))
ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(20800), RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))
ts_data_block.SetData("Position/PositionY", RLPy.RTime(30000), RLPy.RVariant(-9800))
