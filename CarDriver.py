import os, RLPy, math
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *
import random



def GetRandomValueInRange(max, subtractAmount):

    return GetRandomNumber(max, 0) - subtractAmount

def GetRandomNumber(max, increment):

    randomNumber = (random.randint(101771, 124193) % (max)) + increment

    # return value
    return randomNumber

def RegisterCars():

    # create
    cars = []

    for i in range(len(all_props)):        

        name = all_props[i].GetName()

        if (name.startswith("Car")):
        
            cars.append(all_props[i])

    # return value
    return cars

def CreateTraffic():

    # Get the current time
    frameTime = RLPy.RGlobal.GetTime()
    currentTime = frameTime.GetValue()
    
    # currentFrame seems to need the Add 1 to get the current frame value from IClone
    currentFrame = round(currentTime * .001 * 60, 0) + 1

    framesLength = RLPy.RGlobal.GetProjectLength()
    endTime = framesLength.GetValue()
    frames = endTime * .001 * 60

    text_edit.insertPlainText("Current Frame: " + str(currentFrame) + "\r\n");

    text_edit.insertPlainText("Total Frames: " + str(frames) + "\r\n");

    randomOrder = RandomOrderCheckBox.isChecked()

    oneWayTraffic = OneWayCheckBox.isChecked()

    tempCars = RegisterCars()

    cars = []
    
    for i in range(len(tempCars)):

        # create a car
        car = Car()

        # set the properties
        car.Prop = tempCars[i]

        cars.append(car)

    # show number of cars found
    text_edit.insertPlainText("Registered " + str(len(cars)) + " cars." + "\r\n")

    speed = (SpeedSlider.value() * 30)

    # show speed
    text_edit.insertPlainText("Speed: " + str(speed) + "." + "\r\n")

    interval = 9000 - speed;

    # safeguard
    if (interval < 10):
        interval = 10

    # Show interval
    text_edit.insertPlainText("Interval (9,000 - Speed): " + str(interval) + "." + "\r\n")

    congestion = CongestionSlider.value() * 5

    congestionValue = 1000 - congestion

    # show congestion
    text_edit.insertPlainText("Congestion: " + str(congestion) + "%." + "\r\n")

    # if random
    if (randomOrder):

        text_edit.insertPlainText("Cars are displayed in random order.\r\n")

    else:

        text_edit.insertPlainText("Cars are displayed in numerical order. Car1, Car2, etc.\r\n")

    if (oneWayTraffic):

        text_edit.insertPlainText("Traffic will be displayed in one direction.\r\n")

    else:

        text_edit.insertPlainText("Traffic will be displayed in both directions.\r\n")

    
    # show animating message
    text_edit.insertPlainText("Animating cars, please wait...\r\n")

    keyFrames = 0

    while (currentTime < endTime):

        if (randomOrder):
            number = GetRandomNumber(len(cars), -1)
        else:
            number = number + 1

            # if out of range
            if (number >= len(cars)):
                # reset
                number = 0

        # safeguard
        if (number < 0):
            # reset
            number = 0

        car = cars[number]

        # if this car is not already in motion
        if (cars[number].InMotion == False):

            # Set to inmotion to true
            cars[number].InMotion = True

            # show car
            text_edit.insertPlainText("Car " + car.Prop.GetName() + "\r\n")
        
            # setup start position of this car
            posX = -16861.480
            posY = -2270.022
            posZ = 0

            # increment
            keyFrames = keyFrames + 1

            # get a random number between 30 and negative 30
            carStartTime = currentTime + GetRandomNumber(60, -30)

            # set the start time
            cars[number].StartTime = carStartTime

            if (carStartTime < 0):

                # reset
                carStartTime = 0
        
            # show keyFrames added message
            text_edit.insertPlainText("Car start Time: " + str(carStartTime) + ".\r\n")

            # set the prop to the start frame
            PositionProp(car.Prop, posX, posY, posZ, carStartTime, RLPy.ETransitionType_Step, number)

            # get the end time for this car
            carEndTime = carStartTime + interval

            # set the endTime
            cars[number].EndTime = carEndTime

            # show keyFrames added message
            text_edit.insertPlainText("Car End Time: " + str(carEndTime) + ".\r\n")
        
            # setup end position of this car
            posX = 11877.729
            posY = -3702.072
            posZ = 0

            # increment
            keyFrames = keyFrames + 1

            # set the prop to the start frame
            PositionProp(car.Prop, posX, posY, posZ, carEndTime, RLPy.ETransitionType_Linear, number)

            # now increment the current time
            currentTime = currentTime + congestionValue

            # Update the InMotion value
            for i in range (len(cars)):

                # if we have reached end of this car's motion
                # release the car back to idle 
                if (currentTime >= cars[i].EndTime):

                    # this car is no longer in motion
                    cars[i].InMotion = False

                    # show keyFrames added message
                    text_edit.insertPlainText("Car " + cars[i].Prop.GetName() + " finished motion at " + str(currentTime) + "\r\n")


    # show keyFrames added message
    text_edit.insertPlainText("Added " + str(keyFrames) + " key frames.\r\n")

    if (keyFrames > 0):

        # show ready
        text_edit.insertPlainText("Animation finished. Press play to view car animations.\r\n")

    else:

        # show ready
        text_edit.insertPlainText("Zero key frames were added, please debug your script.\r\n")

def ChangeTransitionType(control, currentTime, transitionType):

    # set transition
    control.SetKeyTransition(RLPy.RTime(currentTime), transitionType, 1.0)

def PositionProp(prop, moveX, moveY, moveZ, currentTime, transitionType, number):

    # get access to the control
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

    # now posiiton     
    ts_data_block.SetData("Position/PositionX", RLPy.RTime(currentTime), RLPy.RVariant(moveX))
    ts_data_block.SetData("Position/PositionY", RLPy.RTime(currentTime), RLPy.RVariant(moveY))
    ts_data_block.SetData("Position/PositionZ", RLPy.RTime(currentTime), RLPy.RVariant(moveZ))

    # Change the transition type
    ChangeTransitionType(ts_control, currentTime, transitionType)
    

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Drive Cars")

# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()), QtWidgets.QDockWidget)


dock.setFixedSize(640, 600)

main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)

# checkbox and slider for Glow Channel Strength
RandomOrderCheckBox = QtWidgets.QCheckBox("Random Order")
RandomOrderCheckBox.setChecked(True)

# checkbox and slider for Glow Channel Strength
OneWayCheckBox = QtWidgets.QCheckBox("One Way Traffic")
OneWayCheckBox.setChecked(False)

# Car speedsCar
SpeedSliderLabel = QtWidgets.QLabel("Speed (1 - 100)")
SpeedSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)

# Slower speed takes longer to animate as more passes for each car
SpeedSlider.setRange(1, 100)

SpeedSlider.setSingleStep(1)

# Default to 50
SpeedSlider.setValue(50)

# Car speedsCar
CongestionSliderLabel = QtWidgets.QLabel("Congestion (0 - 100)")
CongestionSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)

# 100 equals = unlimited congestion
CongestionSlider.setRange(0, 100)

CongestionSlider.setSingleStep(1)

# Default to 50
CongestionSlider.setValue(0)

# Button(s) #
CreateTrafficButton = QtWidgets.QPushButton("Create Traffic")
CreateTrafficButton.clicked.connect(CreateTraffic)

# Grab all props in the scene
all_props = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop)

# Margin Label
marginLabel = QtWidgets.QLabel("")

for widget in [progress_bar, text_edit, SpeedSliderLabel, SpeedSlider, CongestionSliderLabel, CongestionSlider, RandomOrderCheckBox, OneWayCheckBox, marginLabel, CreateTrafficButton]:
    main_widget_layout.addWidget(widget)

dockable_window.Show()

# File Info

# Version 1.0.0

# New Features / Fixes: 

class Car:
    def __init__(self):
        self.__Prop = None
        self.__InMotion = False
        self.__StartTime = 0
        self.__EndTime = 0
    def SetProp(self, prop):
        self.__Prop = prop
    def GetProp(self):
        return self.__Prop
    def SetInMotion(self, inMotion):
        self.__InMotion = inMotion
    def GetInMotion(self):
        return self.__InMotion
    def SetStartTime(self, startTime):
        self.__StartTime = startTime
    def GetStartTime(self):
        return self.__StartTime
    def SetEndTime(self, endTime):
        self.__EndTime = endTime
    def GetEndTime(self):
        return self.__EndTime
    Prop=property(GetProp, SetProp)
    InMotion=property(GetInMotion, SetInMotion)
    StartTime=property(GetStartTime, SetStartTime)
    EndTime=property(GetEndTime, SetEndTime)