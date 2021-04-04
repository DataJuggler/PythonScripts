import os, RLPy, math
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *

def ChangeTransitionType(control, currentTime):

    key = RLPy.RTransformKey()
    key.SetTime(RLPy.RTime(currentTime))
    key.SetTransitionType(RLPy.ETransitionType_Linear)
    
    # add this key
    control.AddKey(key, 0)
    
def RotateSphere(control, dataBlock, lastEndTime, startRotation, endRotation):

    # Setup the frame after the last end time
    startTime = lastEndTime

    # make it faster by lowering this number or slower by increasing it
    speed = 540

    ##-- Set Rotation Z
    dataBlock.SetData("Rotation/RotationX", RLPy.RTime(startTime), RLPy.RVariant(startRotation * RLPy.RMath.CONST_DEG_TO_RAD))

    # change the TransitionType
    #ChangeTransitionType(control, startTime)

    # now set the endTime
    endTime = startTime + speed

    ##-- Set Rotation Z
    dataBlock.SetData("Rotation/RotationX", RLPy.RTime(endTime), RLPy.RVariant(endRotation * RLPy.RMath.CONST_DEG_TO_RAD))

    #  change the TransitionType
    #ChangeTransitionType(control, endTime)

    # now set the endTime
    endTime = endTime + speed

    ##-- Set Rotation Z
    dataBlock.SetData("Rotation/RotationX", RLPy.RTime(endTime), RLPy.RVariant(startRotation * RLPy.RMath.CONST_DEG_TO_RAD))

    # change the TransitionType
    #ChangeTransitionType(control, endTime)

    # return value
    return endTime   

def RotateSpheres():

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

    # show the user another message
    text_edit.insertPlainText("Creating Sphere Animation. Please wait..." + "\r\n");
    
    # Get Cylinder1
    sourcePropName = "Cylinder1"
    cylinder1 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, sourcePropName)
    
    # Get Cylinder5
    sourcePropName = "Cylinder5"
    cylinder5 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, sourcePropName)

    # get access to the control

    # Cylinder1
    cylinder1Control = cylinder1.GetControl("Transform")
    cylinder1DataBlock = cylinder1Control.GetDataBlock()

    # Cylinder5
    cylinder5Control = cylinder5.GetControl("Transform")
    cylinder5DataBlock = cylinder5Control.GetDataBlock()

    # values for the rotate
    cylinderDefault = 0
    cylinder1Open = -42
    cylinder5Open = 42

    while (currentTime < endTime):

        # Rotate Cylinder 5 to open and back to close
        currentTime = RotateSphere(cylinder5Control, cylinder5DataBlock, currentTime, cylinderDefault,  cylinder5Open)

        # increment the value for loop
        loop += 1

        if (currentTime > endTime):

            # exit loop
            break

        # Rotate Cylinder 5 to open and back to close
        currentTime = RotateSphere(cylinder1Control, cylinder1DataBlock, currentTime, cylinderDefault,  cylinder1Open)

        # increment the value for loop
        loop += 1

    #   message
    message = "Your Newtown's Cradle is ready." + "\r\n"

    text_edit.insertPlainText(message);

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Newton's Cradle Python Widget")

# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()), QtWidgets.QDockWidget)

dock.setFixedSize(800, 480)

main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

text_edit = QtWidgets.QTextEdit(readOnly=True)
NumberRowsToCreateLabel = QtWidgets.QLabel("Add the Newton's Cradle prop to your scene before clicking the 'Rotate Spheres' button.")

# Buttons #
RotateSpheresButton = QtWidgets.QPushButton("Rotate Spheres")
RotateSpheresButton.clicked.connect(RotateSpheres)

# Margin Label
marginLabel = QtWidgets.QLabel("")

for widget in [NumberRowsToCreateLabel, text_edit, marginLabel, RotateSpheresButton]:
    main_widget_layout.addWidget(widget)

dockable_window.Show()

# File Info

# Version 1.0.0
# New Features / Fixes: 
# This is the 1st version

# Copyright 2021 Corby Nichols / aka Data Juggler
# This is a free prop and Python script. You are welcome to share this file if you like.