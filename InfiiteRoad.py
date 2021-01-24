import os, RLPy, math
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance


def CreateRoads():
    text_edit.clear()
    
    text_edit.insertPlainText("Creating Road Segments. Please Wait." + "\r\n")
    RoadSegments = 0

    # Road Segment Size
    SegmentSize = 400
    
   #-- Get iClone 7 default template path --#
    Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    RawKey = OpenKey(Registry, r"SOFTWARE\Reallusion\iClone\7.0")
    ic_template_path = os.path.abspath(QueryValueEx(RawKey, "Template Data" )[0])

    #-- Load Box_001.iProp --#
    RLPy.RFileIO.LoadFile(ic_template_path + "//iClone Template//Props//3D Blocks//Box_001.iProp")

    #-- Get Prop --#
    prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Box_001")
    
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

    ts_data_block.SetData("Scale/ScaleZ", RLPy.RTime(0), RLPy.RVariant(.04))
    
    # .01 Because 1 = 100%. 400 = 4. The image looks a little stretched if you go too big on one segment.
    ts_data_block.SetData("Scale/ScaleY", RLPy.RTime(0), RLPy.RVariant(SegmentSize * .01))
    
    material_component = prop.GetMaterialComponent()
    mesh_list = prop.GetMeshNames()
    mesh_name = mesh_list[0]
    material_list = material_component.GetMaterialNames(mesh_name)
    material_name = material_list[0]

    #Load image to material channel
    texture_channel = RLPy.EMaterialTextureChannel_Diffuse
    image_file = "C:\\Graphics\\Textures\Asphalt With 4 Stripes.png"
    result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, image_file)
    RoadSegments += 1
    
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

    propName = "Box_001"
    prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, propName)    
    prop.SetName("Road")

    for i in range(1, 40):
        prop2 = prop.Clone()       
        
        newName = "Road" + str(i + 1)
        prop2.SetName(newName)
        ts_control = prop2.GetControl("Transform")
        ts_data_block = ts_control.GetDataBlock()
        RoadSegments += 1

        #-- Set Potation Z To -104 which is a little more than 90 degrees open so the dealers hands doesn't get in the way picking up cards #    
        ts_data_block.SetData("Position/PositionY", RLPy.RTime(0), RLPy.RVariant(SegmentSize * i))

    text_edit.insertPlainText("Created " + str(RoadSegments) + " road segments." + "\r\n")

    camera = RLPy.RScene.FindObject(RLPy.EObjectType_Camera, "Camera")

    # Set the camera transform values for start of video
    control = camera.GetControl("Transform")
    transform = RLPy.RTransform.IDENTITY
    transform.T().x = -4.194
    transform.T().y = -234.552
    transform.T().z = 18.132
    time = RLPy.RTime(0)
    control.SetValue(time, transform)

    ts_data_block = control.GetDataBlock()

    rotationValue = 90

    #-- Set Rotation Z = by a random amount
    ts_data_block.SetData("Rotation/RotationX", RLPy.RTime(0), RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))

    # update after adding a key
    camera.Update()

    # Set the camera transform values for end of video
    transform.T().x = -6.885
    transform.T().y = 15277.289
    transform.T().z = 12.320
    
    # end of video time - (1800 / 60) * 1,000
    time = RLPy.RTime(30000)
    control.SetValue(time, transform)

    ts_data_block = control.GetDataBlock()

    rotationValue = 90

    #-- Set Rotation Z = by a random amount
    ts_data_block.SetData("Rotation/RotationX", RLPy.RTime(30000), RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))

    # update after adding a key
    camera.Update()

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Python Road Creator")
# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()),
                    QtWidgets.QDockWidget)
dock.setFixedSize(640, 480)
main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)

text_edit2 = QtWidgets.QTextEdit(readOnly=True)
text_edit.insertPlainText("Make sure to create a camera BEFORE you click the Create Roads Button.")

# Buttons #
CreateRoadsButton = QtWidgets.QPushButton("Create Roads")
CreateRoadsButton.clicked.connect(CreateRoads)

for widget in [progress_bar, text_edit2, text_edit, CreateRoadsButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()