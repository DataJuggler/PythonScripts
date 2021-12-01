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

def RepositionCars():

    # Get the props that start with Car
    tempCars = RegisterCars()

    # start position
    posX = -15000
    posY = -2320
    posZ = 0

    cars = []

    # original value, won't fire on the first one
    lastCar = "NotSet"
    
    for i in range(len(tempCars)):

        # create a car
        car = Car()

        # set the properties
        car.Prop = tempCars[i]

        cars.append(car)

    for i in range(len(cars)):

        # get the car at this index
        car = cars[i]

        # get the name of this car
        name = car.Prop.GetName()

        # if this car, or the last car was car 17 or car 6, these cars are longer
        if ((name == "Car6") or (name =="Car17")):

            # the last car was bigger
            posX = posX - 360

            # adjust a little left extra also
            posY = posY + 20    

        if ((lastCar == "Car6") or (lastCar == "Car17")):

            # the last car was bigger
            posX = posX - 240

            # adjust a little left extra also
            posY = posY + 10    

        # line the cars up behind each other
        posX = posX - 600

        # adjust a little left each car
        posY = posY + 30

        # position the prop
        PositionProp(car.Prop, posX, posY, posZ, 0, RLPy.ETransitionType_Step, 0)     

        # set name
        lastCar = name

    # show number of cars found
    text_edit.insertPlainText("Parked " + str(len(cars)) + " cars." + "\r\n")    

def CreateTraffic():

    # Get the current time
    frameTime = RLPy.RGlobal.GetTime()
    currentTime = frameTime.GetValue()
    
    # currentFrame seems to need the Add 1 to get the current frame value from IClone
    currentFrame = round(currentTime * .001 * 60, 0) + 1

    framesLength = RLPy.RGlobal.GetProjectLength()
    endTime = framesLength.GetValue()
    frames = endTime * .001 * 60

    # text_edit.insertPlainText("Current Frame: " + str(currentFrame) + "\r\n");

    # text_edit.insertPlainText("End Time: " + str(endTime) + "\r\n");

    # text_edit.insertPlainText("Total Frames: " + str(frames) + "\r\n");

    randomOrder = RandomOrderCheckBox.isChecked()

    oneWayTraffic = OneWayCheckBox.isChecked()

    # Get the props that start with Car
    tempCars = RegisterCars()

    cars = []
    
    for i in range(len(tempCars)):

        # create a car
        car = Car()

        # set the properties
        car.Prop = tempCars[i]

        cars.append(car)

    # show number of cars found
    # text_edit.insertPlainText("Registered " + str(len(cars)) + " cars." + "\r\n")

    speed = (SpeedSlider.value() * 180)

    # show speed
    # text_edit.insertPlainText("Speed: " + str(speed) + "." + "\r\n")

    interval = 36000 - speed;

    # safeguard
    if (interval < 10):
        interval = 10

    # Show interval
    # text_edit.insertPlainText("Interval (18,000 - Speed): " + str(interval) + "." + "\r\n")

    congestion = CongestionSlider.value() * 5

    congestionValue = 1000 - congestion

    # show congestion
    # text_edit.insertPlainText("Congestion: " + str(congestion) + "%." + "\r\n")

    ## if random
    #if (randomOrder):

    #    text_edit.insertPlainText("Cars are displayed in random order.\r\n")

    #else:

    #    text_edit.insertPlainText("Cars are displayed in numerical order. Car1, Car2, etc.\r\n")

    #if (oneWayTraffic):

    #    text_edit.insertPlainText("Traffic will be displayed in one direction.\r\n")

    #else:

    #    text_edit.insertPlainText("Traffic will be displayed in both directions.\r\n")

    
    # show animating message
    # text_edit.insertPlainText("Animating cars, please wait...\r\n")

    keyFrames = 0

    # used for positioning
    posX = 0
    posY = 0
    posZ = 0
    posX2 = 0
    posY2 = 0
    posZ2 = 0
    direction = 0

    if (oneWayTraffic):

        # show animating message
        # text_edit.insertPlainText("One way traffic. Direction: " + str(direction) + "\r\n")

        # get a 0 or a 1
        direction = GetRandomNumber(2, 0)

        if (direction == 0):
            
            # left to right

            # show animating message
            text_edit.insertPlainText("One way traffic. Direction: Left To Right\r\n")

            # start position
            posX = -16861.480
            posY = -2270.022
            posZ = 0

            # end position                    
            posX2 = 11877
            posY2 = -3702
            posZ2 = 0
            
        else:

            # right to left

            # show animating message
            # text_edit.insertPlainText("One way traffic. Direction: Right To Left\r\n")

            # start position
            posX = 11877.729
            posY = -3240.758
            posZ = 0

            #end position
            posX = -16861
            posY = -1756.000
            posZ = 0

            # rotate the prop
            
            # ts_data_block.SetData("Rotation/RotationY",  RLPy.RTime(0), RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))

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
            # text_edit.insertPlainText("Car " + car.Prop.GetName() + "\r\n")

            # if traffic is two way
            if (not oneWayTraffic):

                # traffic goes in both directions

                # get a 0 or a 1
                direction = GetRandomNumber(2, 0)

                # show animating message
                # text_edit.insertPlainText("Two way traffic. Direction: " + str(direction) + "\r\n")

                if (direction == 0):

                    # show animating message
                    # text_edit.insertPlainText("Two way traffic. Direction: Left To Right\r\n")
        
                    # setup start position of this car
                    posX = -16861.480
                    posY = -2270.022
                    posZ = 0

                elif (direction == 1):

                    # show animating message
                    # text_edit.insertPlainText("Two way traffic. Direction: Right To Left\r\n")

                    # change to right to left start position
                    posX = 11877.729
                    posY = -3240.758
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
            # text_edit.insertPlainText("Car start Time: " + str(carStartTime) + ".\r\n")

            # Show this car before the prop starts
            car.Prop.SetVisible(RLPy.RTime(carStartTime - 1), True)

            # set the prop to the start frame
            PositionProp(car.Prop, posX, posY, posZ, carStartTime, RLPy.ETransitionType_Step, direction)

            # get the end time for this car
            carEndTime = carStartTime + interval

            # set the endTime
            cars[number].EndTime = carEndTime

            # show keyFrames added message
            # text_edit.insertPlainText("Car End Time: " + str(carEndTime) + ".\r\n")

            if (not oneWayTraffic):
        
                if (direction == 0):

                    # left to right
        
                    # end position                    
                    posX2 = 11877
                    posY2 = -3702
                    posZ2 = 0

                elif (direction == 1):

                    # right to left

                    # end position                    
                    posX2 = -16861
                    posY2 = -1756.000
                    posZ2 = 0

            # increment
            keyFrames = keyFrames + 1

            # set the prop to the start frame
            PositionProp(car.Prop, posX2, posY2, posZ2, carEndTime, RLPy.ETransitionType_Linear, direction)

            # now increment the current time
            currentTime = int(currentTime + congestionValue)

            # Hide this car after the prop finishes
            car.Prop.SetVisible(RLPy.RTime(carEndTime + 1), False)

            # show current time
            # text_edit.insertPlainText("Current Time: " + str(currentTime) + "\r\n")            

        else:

            # now increment the current time a little, else an infinite loop crashes IClone
            currentTime = int(currentTime + (congestionValue * .1))
            
            # show current time
            # text_edit.insertPlainText("Current Time: " + str(currentTime) + "\r\n")

        # Recycle cars - update the InMotion value if Time has expired
        for i in range (len(cars)):

            # if we have reached end of this car's motion
            # release the car back to idle 
            if ((cars[i].InMotion) and (currentTime >= cars[i].EndTime)):

                # this car is no longer in motion
                cars[i].InMotion = False

                # show keyFrames added message
                # text_edit.insertPlainText(cars[i].Prop.GetName() + " finished motion at " + str(currentTime) + "\r\n")

    # show keyFrames added message
    # text_edit.insertPlainText("Added " + str(keyFrames) + " key frames.\r\n")

    #if (keyFrames > 0):

    #    # show ready
    #    # text_edit.insertPlainText("Animation finished. Press play to view car animations.\r\n")

    #else:

    #    # show ready
    #    text_edit.insertPlainText("Zero key frames were added, please debug your script.\r\n")

def ChangeTransitionType(control, currentTime, transitionType):

    # set transition
    control.SetKeyTransition(RLPy.RTime(currentTime), transitionType, 1.0)

def PositionProp(prop, moveX, moveY, moveZ, currentTime, transitionType, direction):

    # show number of cars found
    text_edit.insertPlainText("Prop: " + prop.GetName() + "\r\n")    
    text_edit.insertPlainText("PositionX: " + str(moveX) + "\r\n")    
    text_edit.insertPlainText("PositionY: " + str(moveY) + "\r\n")    
    text_edit.insertPlainText("PositionZ: " + str(moveZ) + "\r\n")    
    text_edit.insertPlainText("Current Time: " + str(currentTime) + "\r\n")    
    text_edit.insertPlainText("Direction: " + str(direction) + "\r\n")    

    # get access to the control
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()    

    # now posiiton     
    ts_data_block.SetData("Position/PositionX", RLPy.RTime(currentTime), RLPy.RVariant(moveX))
    ts_data_block.SetData("Position/PositionY", RLPy.RTime(currentTime), RLPy.RVariant(moveY))
    ts_data_block.SetData("Position/PositionZ", RLPy.RTime(currentTime), RLPy.RVariant(moveZ))

    time = RLPy.RTime(currentTime)
    transform = RLPy.RTransform()
    ts_control.GetValue(time, transform)
    rotationZ = transform.R().z # Get Prop Z Rotation

    if ((direction == 1) and (rotationZ != 180)):
        
        # rotate 180
        transform.R().z = 180
        ts_control.SetValue(time, transform)

    elif ((direction == 0) and (rotationZ != 0)):

        # reset to original
        transform.R().z = 0
        ts_control.SetValue(time, transform)

    

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

# Button(s) #
RepositionButton = QtWidgets.QPushButton("Reposition Cars")
RepositionButton.clicked.connect(RepositionCars)

# Grab all props in the scene
all_props = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop)

# Margin Label
marginLabel = QtWidgets.QLabel("")

for widget in [progress_bar, text_edit, SpeedSliderLabel, SpeedSlider, CongestionSliderLabel, CongestionSlider, RandomOrderCheckBox, OneWayCheckBox, marginLabel, CreateTrafficButton, RepositionButton]:
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