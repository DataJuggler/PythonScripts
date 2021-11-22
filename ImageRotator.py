import os, RLPy, math, glob
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *

def AddTextToGlowChannelChanged():
    isChecked = addTextToGlowChannelCheckBox.isChecked()
    glowStrengthLabel.setVisible(isChecked)
    glowStrengthSlider.setVisible(isChecked)


def FindSceneProps():
    text_edit.clear()

    text_edit.insertPlainText("Props Found:" + "\r\n")

    # Grab all props in the scene
    all_props = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop)
    
    # Iterate All Props
    for i in range(len(all_props)):
        
        # get this prop
        prop = all_props[i]

        # get the name
        name = prop.GetName()

        # print this prop's name
        text_edit.insertPlainText(name + "\r\n")

def FindProp(all_props, propName):

    for i in range(len(all_props)):        

        name = all_props[i].GetName()

        if (name == propName):
        
            return all_props[i]

def ApplyImages():

    applyMaterial = False

    text_edit.clear()

    # get the range value
    interval = IntervalSlider.value() * 100

    propName = str(combo_box.currentText())

     # Update 3.31.2021: Now the lights are applied at a certain time
    frameTime = RLPy.RGlobal.GetTime()
    currentTime = frameTime.GetValue()
    
    # currentFrame seems to need the Add 1 to get the current frame value from IClone
    currentFrame = round(currentTime * .001 * 60, 0) + 1

    framesLength = RLPy.RGlobal.GetProjectLength()
    endTime = framesLength.GetValue()
    frames = endTime * .001 * 60

    text_edit.insertPlainText("Current Frame: " + str(currentFrame) + "\r\n");

    text_edit.insertPlainText("Total Frames: " + str(frames) + "\r\n");
    
    # find the prop
    prop = FindProp(all_props, propName)

    progress_bar.setRange(1, 100)

    text_edit.insertPlainText("Adding images to prop: " + propName + "\r\n")
    
    # test
    directory = "";
    path = "c:\\Temp\\Images"
    directory = path + "\\*.png";

    print (directory)

    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

    files = []
    
    for file in glob.glob(directory):
        files.append(file)

    text_edit.insertPlainText("Found Files in Directory: " + directory + "\r\n")
    text_edit.insertPlainText(str(len(files)) + "\r\n")

    #text_edit.insertPlainText(propName + "\r\n")
    loops = 0
    index = 0


    while (currentTime < endTime):
        
        loops = loops +1

        index = index + 1

        if (index > 4):
            index = -1

        fileName = files[index]

        print (fileName)
            
        # apply material
        material_component = prop.GetMaterialComponent()
        mesh_list = prop.GetMeshNames()
        mesh_name = mesh_list[0]
        material_list = material_component.GetMaterialNames(mesh_name)
        material_name = material_list[0]

        #Load image to material channel
        texture_channel = RLPy.EMaterialTextureChannel_Diffuse

        diffuse_weight = 1;

        key = RLPy.RKey()
        key.SetTime(RLPy.RTime(currentTime))
            
        result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, fileName)
        material_component.AddTextureWeightKey(key, mesh_name, material_name, texture_channel, diffuse_weight)
        
        if (addTextToGlowChannelCheckBox.isChecked()):
            texture_channel = RLPy.EMaterialTextureChannel_Glow            
            diffuse_weight = glowStrengthSlider.value() * .01
            result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, material_name)
            material_component.AddTextureWeightKey(key, mesh_name, material_name,
                                texture_channel, diffuse_weight)

        
        # add the current time
        currentTime += interval

        # if we are done
        if (currentTime >= endTime):

            # exit while loop
            break
        
        if (loops < 100):
            progress_bar.setValue(loops)

    text_edit.insertPlainText("Result: " + str(loops) + " key frames set \r\n")

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Image Rotator")

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

# Interval
IntervalSliderLabel = QtWidgets.QLabel("Interval Seconds (.1 - 30)")
IntervalSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)

# .1 To 30 Seconds
IntervalSlider.setRange(1, 300)

IntervalSlider.setSingleStep(1)

# Default to 5 Seconds
IntervalSlider.setValue(30)

# checkbox and slider for Glow Channel Strength
addTextToGlowChannelCheckBox = QtWidgets.QCheckBox("Add Texture To Glow Channel")
addTextToGlowChannelCheckBox.stateChanged.connect(AddTextToGlowChannelChanged)
glowStrengthLabel = QtWidgets.QLabel("Glow Strength")
glowStrengthSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)
glowStrengthSlider.setRange(1, 100)
glowStrengthSlider.setSingleStep(10)
glowStrengthSlider.setValue(50)

# hide both by default
glowStrengthLabel.setVisible(False)
glowStrengthSlider.setVisible(False)

# Grab all props in the scene
all_props = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop)


combo_box = QtWidgets.QComboBox()

main_widget_layout.addWidget(combo_box)

# Add an entry into the combo-box for every prop found
for i in range(len(all_props)):
    combo_box.addItem(all_props[i].GetName())


# Buttons #
ApplyImagesButton = QtWidgets.QPushButton("Apply Images")
ApplyImagesButton.clicked.connect(ApplyImages)

# Margin Label
marginLabel = QtWidgets.QLabel("")

for widget in [progress_bar, text_edit, IntervalSliderLabel, IntervalSlider, addTextToGlowChannelCheckBox, glowStrengthLabel, glowStrengthSlider, marginLabel, ApplyImagesButton]:
    main_widget_layout.addWidget(widget)

dockable_window.Show()