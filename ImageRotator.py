import os, RLPy, math, glob
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *

def AddTextToGlowChannelChanged():
    isChecked = addTextToGlowChannelCheckBox.isChecked()
    glowStrengthLabel.setVisible(isChecked)
    glowStrengthSlider.setVisible(isChecked)


def FindProp(all_props, propName):

    for i in range(len(all_props)):        

        name = all_props[i].GetName()

        if (name == propName):
        
            return all_props[i]

def ApplyImages():

    applyMaterial = False

    text_edit.clear()

    # I couldn't do what I wanted, which is apply a texture at keyframes, or I haven't figured that out yet.
    # so what I am doing is making x duplicates of the prop selected, where x = number of files in the directory
    # minus one.

    # get the range value
    interval = IntervalSlider.value() * 15

    print ("interval" + str(interval))

    text_edit.insertPlainText("Interval: " + str(interval) + "\r\n");

    propName = str(combo_box.currentText())

     # Update 3.31.2021: Now the lights are applied at a certain time
    frameTime = RLPy.RGlobal.GetTime()
    currentTime = frameTime.GetValue()
    
    # currentFrame seems to need the Add 1 to get the current frame value from IClone
    currentFrame = round(currentTime * .001 * 60, 0) + 1

    framesLength = RLPy.RGlobal.GetProjectLength()
    endTime = framesLength.GetValue()
    frames = endTime * .001 * 60

    print ("End Time: " + str(endTime))

    text_edit.insertPlainText("Current Frame: " + str(currentFrame) + "\r\n");

    text_edit.insertPlainText("Total Frames: " + str(frames) + "\r\n");
    
    # find the prop
    prop = FindProp(all_props, propName)

    progress_bar.setRange(1, 100)

    text_edit.insertPlainText("Adding images to prop: " + propName + "\r\n")
    
    # test
    directory = "";
    path = directoryChooser.getExistingDirectory()

    directory = path + "\\*.png";

    print (directory)
    
    files = []
    props = []
    
    for file in glob.glob(directory):
        files.append(file)

    text_edit.insertPlainText("Found Files in Directory: " + directory + "\r\n")
    text_edit.insertPlainText(str(len(files)) + "\r\n")

    #text_edit.insertPlainText(propName + "\r\n")
    loops = 0
    index = -1

    props.append(prop)

    # store something for now
    lastProp = prop
    
    # duplicate props
    for i in range(len(files)):
        if (i > 0):
            copy = prop.Clone()
            copy.SetName(prop.GetName() + str(i + 1))
            copy.SetVisible(RLPy.RTime(currentTime), False)
            props.append(copy)            

    firstPass = True
    
    while (currentTime < endTime):
        
        if (firstPass == False):
            loops = loops +1

        index = index + 1

        if (index >= len(files)):
            # reset
            index = 0

            # no longer first pass
            firstPass = False

        fileName = files[index]

        print (fileName)

        thisProp = props[index]
        
        # we only need to apply the images on the first pass
        if (firstPass):

            # apply material
            material_component = thisProp.GetMaterialComponent()
            mesh_list = thisProp.GetMeshNames()
            mesh_name = mesh_list[0]
            material_list = material_component.GetMaterialNames(mesh_name)
            material_name = material_list[0]

            #Load image to material channel
            texture_channel = RLPy.EMaterialTextureChannel_Diffuse

            diffuse_weight = 1;

            key = RLPy.RKey()
            key.SetTime(RLPy.RTime(0))

            result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, fileName)
            material_component.AddTextureWeightKey(key, mesh_name, material_name, texture_channel, diffuse_weight)
        
            if (addTextToGlowChannelCheckBox.isChecked()):                
                texture_channel = RLPy.EMaterialTextureChannel_Glow                
                diffuse_weight = glowStrengthSlider.value() * .01
                result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, fileName)
                material_component.AddTextureWeightKey(key, mesh_name, material_name, texture_channel, diffuse_weight)
        else:

            # Set the last prop to invisible
            lastProp.SetVisible(RLPy.RTime(currentTime), False)

            # Show this prop
            thisProp.SetVisible(RLPy.RTime(currentTime), True)

            # Now set the new lastProp
            lastProp = thisProp            
        
        if (firstPass == False):
            # add the current time
            currentTime += interval

        # if we are done
        if (currentTime >= endTime):

            # exit while loop
            break

        else:
            # testing how far it gets
            print ("Current Time: " + str(currentTime))
            
        if (loops < 100):
            progress_bar.setValue(loops)
        elif(loops == 100):
            text_edit.insertPlainText("Finishing up...\r\n")

    # The parent has to be set after all the keyframes are set
    text_edit.insertPlainText("Setting child props. Almost done...\r\n")

    for i in range(len(props)):
        if (i > 0):
            prop = props[i]
            prop.SetParent(props[0])

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

directoryChooser = QtWidgets.QFileDialog();
directoryChooser.FileMode = QtWidgets.QFileDialog.Directory
directoryChooser.Options = QtWidgets.QFileDialog.ShowDirsOnly
directoryChooser.setWindowTitle('Select folder containing your images')

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