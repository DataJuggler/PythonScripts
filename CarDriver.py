import os, RLPy, math
from typing import Text
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *
import random

class Car:
    def __init__(self):
        self.__Prop = None
        self.__EndTime = 0
        self.__InMotion = False
        self.__Name = ""
        self.__StartTime = 0
        self.__WheelsRotated = False
    def SetProp(self, prop):
        self.__Prop = prop
    def GetProp(self):
        return self.__Prop
    def SetEndTime(self, endTime):
        self.__EndTime = endTime
    def GetEndTime(self):
        return self.__EndTime
    def SetInMotion(self, inMotion):
        self.__InMotion = inMotion
    def GetInMotion(self):
        return self.__InMotion
    def SetName(self, name):
        self.__Name = name
    def GetName(self):
        return self.__Name
    def SetStartTime(self, startTime):
        self.__StartTime = startTime
    def GetStartTime(self):
        return self.__StartTime
    def SetWheelsRotated(self, wheelsRotated):
        self.__WheelsRotated = wheelsRotated
    def GetWheelsRotated(self):
        return self.__WheelsRotated
    Prop=property(GetProp, SetProp)
    EndTime=property(GetEndTime, SetEndTime)
    InMotion=property(GetInMotion, SetInMotion)
    Name=property(GetName, SetName)
    StartTime=property(GetStartTime, SetStartTime)
    WheelsRotated=property(GetWheelsRotated, SetWheelsRotated)

class PropInfo:
    def __init__(self):
        self.__Prop = None
        self.__Name = ""
        self.__Index = 0
    def SetProp(self, prop):
        self.__Prop = prop
    def GetProp(self):
        return self.__Prop
    def SetName(self, name):
        self.__Name = name
    def GetName(self):
        return self.__Name
    def SetIndex(self, index):
        self.__Index = index
    def GetIndex(self):
        return self.__Index
    Prop=property(GetProp, SetProp)
    Name=property(GetName, SetName)
    Index=property(GetIndex, SetIndex)

def GetRandomValueInRange(max, subtractAmount):

    return GetRandomNumber(max, 0) - subtractAmount

def GetRandomNumber(max, increment):

    randomNumber = (random.randint(101771, 124193) % (max)) + increment

    # return value
    return randomNumber

def RegisterCars():

    # create
    cars = []

    for i in range(len(Props)):

        # get the name
        name = Props[i].Name

        if (name.startswith("Car")):
        
            # add this Prop
            cars.append(Props[i])

    # return value
    return cars

def GetWheels(carName):

    # initial value
    wheels = []  

    if (Props is not None):

        # iterate the Props
        for i in range(len(Props)):        

            # get the name of this prop
            name = Props[i].Name

            # if the text ends in the car name and name starts with Wheel
            if ((name.endswith(carName) and (name.startswith("Wheel")))):

                # add this object
                wheels.append(Props[i])
    else:

        text_edit.insertPlainText("Props does not exist in GetWheels method" + ".\r\n")

    # return value
    return wheels

def GetAllWheels():

    # initial value
    wheels = []

    # if the props exist
    if (Props is not None):        

        # iterate the Props
        for i in range(len(Props)):

            # get the name of this prop
            name = Props[i].Name

            # if this is a wheel
            if (name.startswith("Wheel")):

                # add this wheel
                wheels.append(Props[i])

        text_edit.insertPlainText("Wheels found: " + str(len(wheels)) + "\r\n")

    else:

        text_edit.insertPlainText("Props do not exist in GetAllWheels method." + "\r\n")

    # return value
    return wheels

def RotateWheels(car, wheels, direction, startTime, endTime):

    # get the rotation speed
    rotationSpeed = (SpeedSlider.value() * 8)

    # get a number to use for frames, not the actual frames
    frames = int(endTime - startTime)

    text_edit.insertPlainText("Frames: " + str(frames) + "\r\n")
 
    # if the wheels exists
    if (wheels is not None):

        for x in range(len(wheels)):

            # get the wheel name   
            wheel = wheels[x]

            ts_control = wheel.Prop.GetControl("Transform")
            ts_data_block = ts_control.GetDataBlock()  

            # get the rotation value for this prop  
            transform = RLPy.RTransform()
            ts_control.GetValue(RLPy.RTime(startTime), transform)
            rotationY = transform.R().y # Get Prop Y Rotation

            if (direction == 0):

                # get the rotation value
                rotationValue = rotationY + (127 * frames * rotationSpeed)

            else:

                rotationValue = rotationY - (127 * frames * rotationSpeed)

            #-- Set Rotation Z = by a random amount
            ts_data_block.SetData("Rotation/RotationY", RLPy.RTime(endTime), RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))

            # Change the TransitionType
            ChangeTransitionType(ts_control, endTime, RLPy.ETransitionType_Linear)

            # set the parent
            wheel.Prop.SetParent(car.Prop)
        
def RepositionCars():

    # Get the props that start with Car
    tempCars = RegisterCars()

    # start position
    posX = -15000
    posY = -2320
    posZ = 0

    cars = GetCars()

    # initial value
    lastCar = ""

    if (cars is not None):

        for i in range(len(cars)):

            # get the car at this index
            car = cars[i]

            # show each car for this, they get hidden next time it starts
            car.Prop.SetVisible(RLPy.RTime(0), True)

            # get a local reference to the name of this car
            name = car.Name

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

def GetCars():

    cars = []

    # Get the props that start with Car
    tempCars = RegisterCars()

    # if the cars were found
    if (tempCars is not None):
    
        for i in range(len(tempCars)):

            # create a car
            car = Car()

            # set the properties
            car.Prop = tempCars[i].Prop

            # add the name
            car.Name = tempCars[i].Name

            # hide all cars at the start
            car.Prop.SetVisible(RLPy.RTime(0), False)

            cars.append(car)

    # return value
    return cars

def CreateTraffic():

    # get all the props that start with Car
    cars = GetCars()

    if (cars is not None):

        # Get the current time
        frameTime = RLPy.RGlobal.GetTime()
        currentTime = frameTime.GetValue()
    
        # currentFrame seems to need the Add 1 to get the current frame value from IClone
        currentFrame = round(currentTime * .001 * 60, 0) + 1

        framesLength = RLPy.RGlobal.GetProjectLength()
        endTime = framesLength.GetValue()
        frames = endTime * .001 * 60

        randomOrder = RandomOrderCheckBox.isChecked()

        oneWayTraffic = OneWayCheckBox.isChecked()
    
        # show number of cars found
        # text_edit.insertPlainText("Registered " + str(len(cars)) + " cars." + "\r\n")

        speed = (SpeedSlider.value() * 40)

        # show speed
        # text_edit.insertPlainText("Speed: " + str(speed) + "." + "\r\n")

        interval = 36000 - speed;

        # safeguard
        if (interval < 10):
            interval = 10

        congestion = CongestionSlider.value() * 10

        congestionValue = 2000 - congestion    

        # get the end time for this car
        carEndTime = currentTime + interval

        # local
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

        progress_bar.setRange(1, endTime)

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

                if (carStartTime < 1):

                    # reset
                    carStartTime = 1

                # get the end time for this car
                carEndTime = carStartTime + interval

                # set the start time
                cars[number].StartTime = carStartTime

                # set the endTime
                cars[number].EndTime = carEndTime

                # show keyFrames added message
                text_edit.insertPlainText("Preparing to rotate wheels for car: " + car.Name + ".\r\n")

                # if the wheels have NOT been rotated yet
                if (not cars[number].WheelsRotated):

                    # get the wheels for this car
                    wheels = GetWheels(car.Name)

                    # rotate this wheel
                    RotateWheels(cars[number], wheels, direction, carStartTime, endTime)

                    # Toggle
                    cars[number].WheelsRotated = True

                # show keyFrames added message
                text_edit.insertPlainText("Rotated wheels for car: " + car.Name + ".\r\n")
        
                # show keyFrames added message
                # text_edit.insertPlainText("Car start Time: " + str(carStartTime) + ".\r\n")

                # Show this car before the prop starts
                car.Prop.SetVisible(RLPy.RTime(carStartTime - 1), True)
            
                # show keyFrames added message
                text_edit.insertPlainText("Preparing to position car at start for car: " + car.Name + ".\r\n")

                # set the prop to the start frame
                PositionProp(car.Prop, posX, posY, posZ, carStartTime, RLPy.ETransitionType_Step, direction)

                # show keyFrames added message
                text_edit.insertPlainText("Start position set for car: " + car.Name + ".\r\n")

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
                text_edit.insertPlainText("Current Time: " + str(currentTime) + "\r\n")            

            else:

                # now increment the current time a little, else an infinite loop crashes IClone
                currentTime = int(currentTime + (congestionValue * .1))
            
                # show current time
                text_edit.insertPlainText("Current Time: " + str(currentTime) + "\r\n")

            # if not the max yet
            if (currentTime < endTime):

                # update progress
                progress_bar.setValue(currentTime);

            else:

                # set to max
                progress_bar.setValue(endTime);

            # Recycle cars - update the InMotion value if Time has expired
            for i in range (len(cars)):

                # if we have reached end of this car's motion
                # release the car back to idle 
                if ((cars[i].InMotion) and (currentTime >= cars[i].EndTime)):

                    # this car is no longer in motion
                    cars[i].InMotion = False
        
   
def ChangeTransitionType(control, currentTime, transitionType):

    # set transition
    control.SetKeyTransition(RLPy.RTime(currentTime), transitionType, 1.0)

def ConvertProps(all_props):
    
    # initial value
    props = []

    # counter
    count = 0

    # ensure the all_props exist
    if (all_props is not None):

        # iterate all_props
        for i in range (len(all_props)):

            # create a new class
            prop = PropInfo()
            
            # set the properties
            prop.Prop = all_props[i]
            prop.Name = prop.Prop.GetName()
            prop.Index = count

            # add this item
            props.append(prop)

            # increment
            count = count + 1

    # return value
    return props

def ResetPivot():

    # get all the wheels
    wheels = GetAllWheels()

    if ((wheels is not None) and (len(wheels) > 0)):

        progress_bar.setRange(1, len(wheels))

        for i in range (len(wheels)):

            wheel = wheels[i]
            
            ts_control = wheel.Prop.GetControl("Transform")
            time = RLPy.RTime()
            transform_for_ref = RLPy.RTransform()
            ts_control.GetValue(time, transform_for_ref)
            posX = transform_for_ref.T().x # Get Prop X Position
            posY = transform_for_ref.T().y # Get Prop Y Position
            posZ = transform_for_ref.T().z # Get Prop Z Position            

            #set pivot, keep rotation to existing position
            pos = RLPy.RVector3(posX, posY, posZ)
            rot = RLPy.RVector3(0, 0, 0)
            wheel.Prop.SetPivot(pos, rot)

            # update the graph
            progress_bar.setValue(i + 1);

        text_edit.insertPlainText("Reset " + str(len(wheels)) + " wheels.\r\n")

    else:

        # show a message
        text_edit.insertPlainText("No wheels were found.\r\n")

def AttachWheels():

    # get the cars
    cars = GetCars()

    # local
    count = 0

    if (cars is not None):

         for i in range (len(cars)):
    
            # get this car
            car = cars[i]

            # Get the wheels
            wheels = GetWheels(car.Name)

            if (wheels is not None):

                for i in range (len(wheels)):

                    # get a reference to this wheel
                    wheel = wheels[i]

                    # set the parent
                    wheel.Prop.SetParent(car.Prop)
    
                    # increment
                    count = count + 1

            # Show the car
            car.Prop.SetVisible(RLPy.RTime(0), True)

    # show a message
    text_edit.insertPlainText("Wheels attached: " + str(count) + ".\r\n")

def LoadProps():

    # convert the props
    props = ConvertProps(all_props)

    # if the props were found
    if ((Props is not None) and (len(props) > 0)):

        CreateTrafficButton.setEnabled(True)
        RepositionButton.setEnabled(True)
        ResetPivotButton.setEnabled(True)
        AttachWheelsButton.setEnabled(True)

        # Show a message
        text_edit.insertPlainText("Loaded " + str(len(props)) + " props.\r\n")

        # show a message the program is ready to use
        text_edit.insertPlainText("Ready." + "\r\n")

    else:

        # Should never happen
        text_edit.insertPlainText("Something went wrong." + "\r\n")

    return props

def PositionProp(prop, moveX, moveY, moveZ, currentTime, transitionType, direction):

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

# 100 equals = more congestion (interval between cars)
CongestionSlider.setRange(0, 100)

CongestionSlider.setSingleStep(1)

# Default to 50
CongestionSlider.setValue(0)

# Button to create the traffic animation
CreateTrafficButton = QtWidgets.QPushButton("Create Traffic")
CreateTrafficButton.clicked.connect(CreateTraffic)
CreateTrafficButton.setEnabled(False)

# Button to line up the cars
RepositionButton = QtWidgets.QPushButton("Reposition Cars")
RepositionButton.clicked.connect(RepositionCars)
RepositionButton.setEnabled(False)

# Rename Wheels
ResetPivotButton = QtWidgets.QPushButton("Reset Pivot")
ResetPivotButton.clicked.connect(ResetPivot)
ResetPivotButton.setEnabled(False)

# Rename Wheels
AttachWheelsButton = QtWidgets.QPushButton("Attach Wheels")
AttachWheelsButton.clicked.connect(AttachWheels)
AttachWheelsButton.setEnabled(False)

# Grab all props in the scene
all_props = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop)

# Has To Be Loaded Later For Some Reason
Props = []

# Margin Label
marginLabel = QtWidgets.QLabel("")

for widget in [progress_bar, text_edit, SpeedSliderLabel, SpeedSlider, CongestionSliderLabel, CongestionSlider, RandomOrderCheckBox, OneWayCheckBox, marginLabel, CreateTrafficButton, RepositionButton, ResetPivotButton, AttachWheelsButton]:
    main_widget_layout.addWidget(widget)

dockable_window.Show()

# Load the PropInfo objects
Props = LoadProps()

# File Info

# Version 1.0.0

# New Features / Fixes: 

