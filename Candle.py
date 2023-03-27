import os, RLPy, math, random
from winreg import *
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
from PySide2.QtCore import *

ap_version=RLPy.RApplication.GetProductVersion()[0]
if ap_version == 7:
    rl_plugin_info = {"ap": "iClone", "ap_version": "7.0"}
if ap_version == 8:
    rl_plugin_info = {"ap": "iClone", "ap_version": "8.0"}

def GetFlame():
    text_edit.clear()

    # Grab all props in the scene
    all_props = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop)

    totalProps = len(all_props)

    print ("Total Props: " + str(totalProps))
    
    # Iterate All Props
    for i in range(totalProps):
        
        # get this prop
        prop = all_props[i]

        # get the name
        name = prop.GetName()

        print ("Prop Name: " + name)

        if (name == "FLAME"):

            return prop


def GetRandomValueInRange(max, subtractAmount):

    return GetRandomNumber(max, 0) - subtractAmount

def GetRandomNumber(max, increment):

    randomNumber = (random.randint(101771, 124193) % (max)) + increment

    # return value
    return randomNumber

def ScaleProp(prop, scaleX, scaleY, scaleZ, currentTime):

    # get access to the control
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

     # now scale     
    ts_data_block.SetData("Scale/ScaleX", RLPy.RTime.FromValue(currentTime), RLPy.RVariant(scaleX))
    ts_data_block.SetData("Scale/ScaleY", RLPy.RTime.FromValue(currentTime), RLPy.RVariant(scaleY))
    ts_data_block.SetData("Scale/ScaleZ", RLPy.RTime.FromValue(currentTime), RLPy.RVariant(scaleZ))

def AnimateCandle():
    
    # clear everythiing
    text_edit.clear()

    # Update 3.31.2021: Now the lights are applied at a certain time
    frameTime = RLPy.RGlobal.GetTime()
    currentTime = frameTime.GetValue()
    resetTime = currentTime
    
    # currentFrame seems to need the Add 1 to get the current frame value from IClone
    currentFrame = round(currentTime * .001 * 60, 0) + 1

    framesLength = RLPy.RGlobal.GetProjectLength()
    endTime = framesLength.GetValue()
    frames = endTime * .001 * 60

    text_edit.insertPlainText("Current Frame: " + str(currentFrame) + "\r\n")

    text_edit.insertPlainText("Total Frames: " + str(frames) + "\r\n")

    # get the flame (will switch to multiple later)
    flame = GetFlame()

    if (flame is not None):
        text_edit.insertPlainText("Animating Candle, please wait." + "\r\n")
    else:
        text_edit.insertPlainText("You must add one or more candles and detatch the FLAME elements for this script to run." + "\r\n")

        # exit
        return

    # get the range value
    interval = IntervalSlider.value() * 150

    # variables and their ranges
    rotateX = 0
    scaleY = 0
    scaleZ = 0
    rotateX = 0
    rotateY = 0
    rotateZ = 0

    x = 0

    # setup the progress_bar
    totalProgress = round((endTime / interval), 0) + 5
    progress_bar.setRange(1, totalProgress)

    print ("totalProgress: " + str(totalProgress))

    progress = 0
   
    while (currentTime < endTime):

        progress += 1

        progress_bar.setValue(progress)

        # Get random values for rotation and scale

        # scale is .8 to 1.2 range for scale
        scaleX = round((80 + (GetRandomValueInRange(60, 30))) * .01, 2)
        scaleY = round((80 + (GetRandomValueInRange(60, 30))) * .01, 2)
        scaleZ = round((80 + (GetRandomValueInRange(60, 30))) * .01, 2)

        ## if you want to check the values generated, uncomment this. Makes it a little slower probably.
        #print ("scaleX: " + str(scaleX))
        #print ("scaleY: " + str(scaleY))
        #print ("scaleZ: " + str(scaleZ))
       
        ScaleProp(flame, scaleX, scaleY, scaleZ, currentTime)

        # add the current time
        currentTime += interval

    # set the progress bar to finished
    progress_bar.setValue(totalProgress)

    # show a message done
    text_edit.insertPlainText("Finished" + "\r\n")

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Candle Animator")

# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()),
                    QtWidgets.QDockWidget)

dock.setFixedSize(640, 640)

main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

# Interval
IntervalSliderLabel = QtWidgets.QLabel("Speed (1 is faster - 10 is slower flame movement)")
IntervalSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)

# 1 To 30 Seconds
IntervalSlider.setRange(1, 10)

IntervalSlider.setSingleStep(1)

# Default to 5 mid range
IntervalSlider.setValue(5)

text_edit = QtWidgets.QTextEdit(readOnly=True)
text_edit2 = QtWidgets.QTextEdit(readOnly=True)


# Buttons #
AnimateCandleButton = QtWidgets.QPushButton("Animate Candle")
AnimateCandleButton.clicked.connect(AnimateCandle)

# Margin Label
marginLabel = QtWidgets.QLabel("")

progress_bar = QtWidgets.QProgressBar()

# Show instructions
text_edit2.insertPlainText("1. This script works with only 1 unattached FLAME in your scene." + "\r\n")
text_edit2.insertPlainText("2. To work with multiple candles, detach the FLAME from each candle one at a time." + "\r\n")
text_edit2.insertPlainText("3. Reattach the FLAME after you click the 'Animate Candle' button." + "\r\n")
text_edit2.insertPlainText("4. Repeat for as many candles in your scene as you desire. ." + "\r\n")

for widget in [progress_bar, text_edit2, text_edit, marginLabel, IntervalSliderLabel, IntervalSlider, AnimateCandleButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()
