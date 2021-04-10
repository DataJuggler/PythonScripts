import RLPy
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *

def ChangeTransitionType(control, currentTime):

    # set transition
    control.SetKeyTransition(RLPy.RTime(currentTime), RLPy.ETransitionType_Step, 1.0)

def PositionProp(prop, moveX, moveY, moveZ, currentTime):

    # get access to the control
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()

    # now posiiton     
    ts_data_block.SetData("Position/PositionX", RLPy.RTime(currentTime), RLPy.RVariant(moveX))
    ts_data_block.SetData("Position/PositionY", RLPy.RTime(currentTime), RLPy.RVariant(moveY))
    ts_data_block.SetData("Position/PositionZ", RLPy.RTime(currentTime), RLPy.RVariant(moveZ))

    # Change the transition type
    ChangeTransitionType(ts_control, currentTime)

def TeleportBalls():

    # clear in case of a previous use
    text_edit.clear()

    # get the range value
    interval = IntervalSlider.value() * 1000
    
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
    text_edit.insertPlainText("Creating Ball Teleportations. Please wait..." + "\r\n");

    # -- Get Prop 1 --#
    ball1 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Ball1")

    # -- Get Transform Control and Data --#
    ts_control = ball1.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX = transform_for_ref.T().x # Get Prop X position
    propY = transform_for_ref.T().y # Get Prop Y position
    propZ = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 2 --#
    ball2 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Ball2")

    # -- Get Transform Control and Data --#
    ts_control = ball2.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX2 = transform_for_ref.T().x # Get Prop X position
    propY2 = transform_for_ref.T().y # Get Prop Y position
    propZ2 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 3 --#
    ball3 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Ball3")

    # -- Get Transform Control and Data --#
    ts_control = ball3.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX3 = transform_for_ref.T().x # Get Prop X position
    propY3 = transform_for_ref.T().y # Get Prop Y position
    propZ3 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 4 --#
    ball4 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Ball4")

    # -- Get Transform Control and Data --#
    ts_control = ball4.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX4 = transform_for_ref.T().x # Get Prop X position
    propY4 = transform_for_ref.T().y # Get Prop Y position
    propZ4 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 5 --#
    ball5 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Ball5")

    # -- Get Transform Control and Data --#
    ts_control = ball5.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX5 = transform_for_ref.T().x # Get Prop X position
    propY5 = transform_for_ref.T().y # Get Prop Y position
    propZ5 = transform_for_ref.T().z # Get Prop Z position

    # used to keep track of the current index
    index = 0

    while (currentTime < endTime):

        # increment
        index += 1

        # if out of range
        if (index > 4):

            # reset
            index = 0

        # Move Each Ball Each Loop
        if (index == 0):

            # Position Each Ball
            PositionProp(ball1, propX, propY, propZ, currentTime)
            PositionProp(ball2, propX2, propY2, propZ2, currentTime)
            PositionProp(ball3, propX3, propY3, propZ3, currentTime)
            PositionProp(ball4, propX4, propY4, propZ4, currentTime)
            PositionProp(ball5, propX5, propY5, propZ5, currentTime)

        if (index == 1):

            # Position Each Ball
            PositionProp(ball5, propX, propY, propZ, currentTime)
            PositionProp(ball1, propX2, propY2, propZ2, currentTime)
            PositionProp(ball2, propX3, propY3, propZ3, currentTime)
            PositionProp(ball3, propX4, propY4, propZ4, currentTime)
            PositionProp(ball4, propX5, propY5, propZ5, currentTime)

        if (index == 2):

            # Position Each Ball
            PositionProp(ball4, propX, propY, propZ, currentTime)
            PositionProp(ball5, propX2, propY2, propZ2, currentTime)
            PositionProp(ball1, propX3, propY3, propZ3, currentTime)
            PositionProp(ball2, propX4, propY4, propZ4, currentTime)
            PositionProp(ball3, propX5, propY5, propZ5, currentTime)

        if (index == 3):

            # Position Each Ball
            PositionProp(ball3, propX, propY, propZ, currentTime)
            PositionProp(ball4, propX2, propY2, propZ2, currentTime)
            PositionProp(ball5, propX3, propY3, propZ3, currentTime)
            PositionProp(ball1, propX4, propY4, propZ4, currentTime)
            PositionProp(ball2, propX5, propY5, propZ5, currentTime)

        if (index == 4):

            # Position Each Ball
            PositionProp(ball2, propX, propY, propZ, currentTime)
            PositionProp(ball3, propX2, propY2, propZ2, currentTime)
            PositionProp(ball4, propX3, propY3, propZ3, currentTime)
            PositionProp(ball5, propX4, propY4, propZ4, currentTime)
            PositionProp(ball1, propX5, propY5, propZ5, currentTime)

        # add the current time
        currentTime += interval

        # if we are done
        if (currentTime > endTime):

            # exit while loop
            break

    text_edit.insertPlainText("Your Balls Are Ready To Teleport. Press Play." +  "\r\n")

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Ball Teleportatiion Widget")

# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()),
                    QtWidgets.QDockWidget)
dock.setFixedSize(640, 420)
main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

text_edit = QtWidgets.QTextEdit(readOnly=True)

# Interval
IntervalSliderLabel = QtWidgets.QLabel("Interval Seconds (1 - 120)")
IntervalSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)

# 1 To 30 Seconds
IntervalSlider.setRange(1, 30)

IntervalSlider.setSingleStep(1)

# Default to 5 Seconds
IntervalSlider.setValue(5)

# Buttons #
TeleportButton = QtWidgets.QPushButton("Teleport Balls")
TeleportButton.clicked.connect(TeleportBalls)

# Margin Label
marginLabel = QtWidgets.QLabel()


for widget in [text_edit, IntervalSliderLabel, IntervalSlider, marginLabel, TeleportButton]:
    main_widget_layout.addWidget(widget)

dockable_window.Show()