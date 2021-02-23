import os, RLPy, math
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *

def PositionAndScaleProp(prop, scaleX, scaleY, scaleZ, moveX, moveY, moveZ):

    # get access to the control
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

     # now scale     
    ts_data_block.SetData("Scale/ScaleX", RLPy.RTime(0), RLPy.RVariant(scaleX))
    ts_data_block.SetData("Scale/ScaleY", RLPy.RTime(0), RLPy.RVariant(scaleY))
    ts_data_block.SetData("Scale/ScaleZ", RLPy.RTime(0), RLPy.RVariant(scaleZ))

    # now posiiton     
    ts_data_block.SetData("Position/PositionX", RLPy.RTime(0), RLPy.RVariant(moveX))
    ts_data_block.SetData("Position/PositionY", RLPy.RTime(0), RLPy.RVariant(moveY))
    ts_data_block.SetData("Position/PositionZ", RLPy.RTime(0), RLPy.RVariant(moveZ))

def RotateProp(prop, rotateX, rotateY, rotateZ):

    # get access to the control
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

    #-- Set Rotation Z = by a random amount
    ts_data_block.SetData("Rotation/RotationX", RLPy.RTime(0), RLPy.RVariant(rotateX * RLPy.RMath.CONST_DEG_TO_RAD))
    ts_data_block.SetData("Rotation/RotationY", RLPy.RTime(0), RLPy.RVariant(rotateY * RLPy.RMath.CONST_DEG_TO_RAD))
    ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(0), RLPy.RVariant(rotateZ * RLPy.RMath.CONST_DEG_TO_RAD))

def ApplyMaterial(prop, materialPath):

    material_component = prop.GetMaterialComponent()
    mesh_list = prop.GetMeshNames()
    mesh_name = mesh_list[0]
    material_list = material_component.GetMaterialNames(mesh_name)
    material_name = material_list[0]

    #Load image to material channel
    texture_channel = RLPy.EMaterialTextureChannel_Diffuse


    # apply the material
    result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, materialPath)

def CreateChair():
    
    text_edit.clear()
    #-- Get iClone 7 default template path --#
    Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    RawKey = OpenKey(Registry, r"SOFTWARE\Reallusion\iClone\7.0")
    ic_template_path = os.path.abspath(QueryValueEx(RawKey, "Template Data" )[0])
    
    # estimate of 10
    progress_bar.setRange(1, 10)

    fileName = ""
    
    text_edit.insertPlainText("Creating the chair rails. Please Wait." + "\r\n")

    fileName = ic_template_path + "//iClone Template//Props//3D Blocks//Beveled//Rounded_Box.iProp"

    #-- Load iProp --#
    chair = RLPy.RFileIO.LoadObject(fileName)

    # now create the rail
    leftRail = chair.Clone()

    leftRail.SetName("LeftRail")

    # constants for the rail size
    scaleX = .927
    scaleY = .021
    scaleZ = .024

    # constants for the rail position
    moveX = -35.521
    moveY = 68.657
    moveZ = 35.413

    # position and scale the left rail
    PositionAndScaleProp(leftRail, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # apply the material
    ApplyMaterial(leftRail, ChairRailMaterialPath)

    # now clone the rail for leftRail2
    leftRail2 = leftRail.Clone()
    leftRail2.SetName("LeftRail2")

    # just move this prop down
    moveZ = 0.522

    # position and scale the left rail
    PositionAndScaleProp(leftRail2, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now clone the rail for leftRail3
    leftRail3 = leftRail.Clone()
    leftRail3.SetName("LeftRail3")

    # just move this prop down
    moveZ = -14.028

    # position and scale the left rail
    PositionAndScaleProp(leftRail3, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

     # now clone the rail for leftRail4
    leftRail4 = leftRail.Clone()
    leftRail4.SetName("LeftRail4")

    # this prop has to be rotated, moved and scaled
    rotateY = 90
    scaleX = .52
    moveX = -84.556
    moveY = 68.657
    moveZ = 11.845

    # Rotate leftRail 4
    RotateProp(leftRail4, 0, rotateY, 0)

    # position and scale the leftRail4
    PositionAndScaleProp(leftRail4, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now the final rail for the left rail
    leftRail5 = leftRail4.Clone()
    leftRail5.SetName("LeftRail5")

    # The only thing that has to be changed here is the moveX
    moveX = 9.429

    # position and scale the leftRail4
    PositionAndScaleProp(leftRail5, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now set the parents
    leftRail2.SetParent(leftRail)
    leftRail3.SetParent(leftRail)
    leftRail4.SetParent(leftRail)
    leftRail5.SetParent(leftRail)

    # now we are going to clone the leftRail and its sub props to form RightRail
    rightRail = leftRail.Clone()
    rightRail.SetName("RightRail")

    # now position and scale the rightRail
    scaleX = .927
    scaleY = .021
    scaleZ = .024
    moveX = -35.521
    moveY = -65.007
    moveZ = 35.413

    # position and scale the rightRail
    PositionAndScaleProp(rightRail, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now the back rail
    backRail = leftRail.Clone()
    backRail.SetName("BackRail")

    # Now Position and Scale
    scaleX = 1.307
    moveX = 11.049
    moveY = 0.722
    moveZ = 35.413
    rotateZ = 90.000

    # Rotate the backRail
    RotateProp(backRail, 0, 0, rotateZ)

    # position and scale the backRail
    PositionAndScaleProp(backRail, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now setup the Chair
    chair.SetName("Chair")

    # apply the material
    ApplyMaterial(chair, ChairMaterialPath)

    # now scale and position the chair back
    moveX = -2.152
    moveY = 1.6
    moveZ = 0
    scaleX = .244
    scaleY = .94
    scaleZ = .753

    # position and scale the backRail
    PositionAndScaleProp(chair, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now create the chairLeftArm
    chairLeftArm = chair.Clone()
    chairLeftArm.SetName("ChairLeftArm")

    # now rotate chairLeftArm
    rotateX = 0
    rotateY = 0
    rotateZ = 90

    # perform the rotate
    RotateProp(chairLeftArm, rotateX, rotateY, rotateZ)

    # now scale and position chairLeftArm
    moveX = -34.876
    moveY = 59.023
    moveZ = 0
    scaleX = .172
    scaleY = .9
    scaleZ = .541

    # position and scale the chairLeftArm
    PositionAndScaleProp(chairLeftArm, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now create the chairRightArm
    chairRightArm = chairLeftArm.Clone()

    # set the name
    chairRightArm.SetName("ChairRightArm")

    # the only attribute that changes between chairLeftArm and chairRightArm is moveY
    moveY = -55.864

    # position and scale the backRail
    PositionAndScaleProp(chairRightArm, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now create the chair seat
    chairSeat = chair.Clone()
    chairSeat.SetName("ChairSeat")

    # now rotate the chairSeat
    rotateX = 0
    rotateY = 90
    rotateZ = 0

    # perform the rotate
    RotateProp(chairSeat, rotateX, rotateY, rotateZ)

    # now position and scale the chairSeat
    moveX = -83.582
    moveY = 1.600
    moveZ = 13.832
    scaleX = .244
    scaleY = .92
    scaleZ = .716

    # position and scale the backRail
    PositionAndScaleProp(chairSeat, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # now attach all the pieces to the chair prop
    leftRail.SetParent(chair)
    rightRail.SetParent(chair)
    backRail.SetParent(chair)
    chairLeftArm.SetParent(chair)
    chairRightArm.SetParent(chair)
    chairSeat.SetParent(chair)

    # now move the chair
    moveX = -2.152
    moveY = 1.6
    moveZ = 14.2
    scaleX = .244
    scaleY = .92
    scaleZ = .753

    # position and scale the backRail
    PositionAndScaleProp(chair, scaleX, scaleY, scaleZ, moveX, moveY, moveZ)

    # show a message chair created
    text_edit.insertPlainText("Chair created." + "\r\n")

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Chair creator")

# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()),
                    QtWidgets.QDockWidget)

dock.setFixedSize(640, 640)

main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)
textToSpellLabel = QtWidgets.QLabel("Enter Text To Spell")

text_edit2 = QtWidgets.QTextEdit(readOnly=False)

ChairMaterialPath = ""
ChairRailMaterialPath = ""

filedialog = QtWidgets.QFileDialog()
filedialog.setWindowTitle('Select Chair Texture')
filedialog.setNameFilters(["Images (*.png *.jpg)"])
filedialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
if filedialog.exec_() == QtWidgets.QDialog.Accepted:
    ChairMaterialPath = str(filedialog.selectedFiles()[0])

filedialog2 = QtWidgets.QFileDialog()
filedialog2.setWindowTitle('Select Chair Rail Texture')
filedialog2.setNameFilters(["Images (*.png *.jpg)"])
filedialog2.setFileMode(QtWidgets.QFileDialog.ExistingFile)
if filedialog2.exec_() == QtWidgets.QDialog.Accepted:
    ChairRailMaterialPath = str(filedialog2.selectedFiles()[0])  


# Buttons #
CreateChairButton = QtWidgets.QPushButton("Create Chair")
CreateChairButton.clicked.connect(CreateChair)

# Margin Label
marginLabel = QtWidgets.QLabel("")

for widget in [progress_bar, text_edit2, text_edit, marginLabel, CreateChairButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()