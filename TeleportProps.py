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

def TeleportProps():

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
    text_edit.insertPlainText("Creating Prop Teleportations. Please wait..." + "\r\n");

    # -- Get Prop 1 --#
    prop1 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop1")

    # -- Get Transform Control and Data --#
    ts_control = prop1.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX = transform_for_ref.T().x # Get Prop X position
    propY = transform_for_ref.T().y # Get Prop Y position
    propZ = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 2 --#
    prop2 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop2")

    # -- Get Transform Control and Data --#
    ts_control = prop2.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX2 = transform_for_ref.T().x # Get Prop X position
    propY2 = transform_for_ref.T().y # Get Prop Y position
    propZ2 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 3 --#
    prop3 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop3")

    # -- Get Transform Control and Data --#
    ts_control = prop3.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX3 = transform_for_ref.T().x # Get Prop X position
    propY3 = transform_for_ref.T().y # Get Prop Y position
    propZ3 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 4 --#
    prop4 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop4")

    # -- Get Transform Control and Data --#
    ts_control = prop4.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX4 = transform_for_ref.T().x # Get Prop X position
    propY4 = transform_for_ref.T().y # Get Prop Y position
    propZ4 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 5 --#
    prop5 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop5")

    # -- Get Transform Control and Data --#
    ts_control = prop5.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX5 = transform_for_ref.T().x # Get Prop X position
    propY5 = transform_for_ref.T().y # Get Prop Y position
    propZ5 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 6 --#
    prop6 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop6")

    # -- Get Transform Control and Data --#
    ts_control = prop6.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX6 = transform_for_ref.T().x # Get Prop X position
    propY6 = transform_for_ref.T().y # Get Prop Y position
    propZ6 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 7 --#
    prop7 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop7")

    # -- Get Transform Control and Data --#
    ts_control = prop7.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX7 = transform_for_ref.T().x # Get Prop X position
    propY7 = transform_for_ref.T().y # Get Prop Y position
    propZ7 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 8 --#
    prop8 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop8")

    # -- Get Transform Control and Data --#
    ts_control = prop8.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX8 = transform_for_ref.T().x # Get Prop X position
    propY8 = transform_for_ref.T().y # Get Prop Y position
    propZ8 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 9 --#
    prop9 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop9")

    # -- Get Transform Control and Data --#
    ts_control = prop9.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX9 = transform_for_ref.T().x # Get Prop X position
    propY9 = transform_for_ref.T().y # Get Prop Y position
    propZ9 = transform_for_ref.T().z # Get Prop Z position

    # -- Get Prop 10 --#
    prop10 = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, "Prop10")

    # -- Get Transform Control and Data --#
    ts_control = prop10.GetControl("Transform")

    time = RLPy.RTime()
    transform_for_ref = RLPy.RTransform()
    ts_control.GetValue(time, transform_for_ref)
    propX10 = transform_for_ref.T().x # Get Prop X position
    propY10 = transform_for_ref.T().y # Get Prop Y position
    propZ10 = transform_for_ref.T().z # Get Prop Z position

    # used to keep track of the current index
    index = -1

    while (currentTime < endTime):

        # increment
        index += 1

        # if out of range
        if (index > 4):

            # reset
            index = 0

        # Move Each Prop Each Loop
        if (index == 0):

            # Position Each Prop
            PositionProp(prop1, propX, propY, propZ, currentTime)
            PositionProp(prop2, propX2, propY2, propZ2, currentTime)
            PositionProp(prop3, propX3, propY3, propZ3, currentTime)
            PositionProp(prop4, propX4, propY4, propZ4, currentTime)
            PositionProp(prop5, propX5, propY5, propZ5, currentTime)
            PositionProp(prop6, propX6, propY6, propZ6, currentTime)
            PositionProp(prop7, propX7, propY7, propZ7, currentTime)
            PositionProp(prop8, propX8, propY8, propZ8, currentTime)
            PositionProp(prop9, propX9, propY9, propZ9, currentTime)
            PositionProp(prop10, propX10, propY10, propZ10, currentTime)

        if (index == 1):

            # Position Each Prop
            PositionProp(prop10, propX, propY, propZ, currentTime)
            PositionProp(prop1, propX2, propY2, propZ2, currentTime)
            PositionProp(prop2, propX3, propY3, propZ3, currentTime)
            PositionProp(prop3, propX4, propY4, propZ4, currentTime)
            PositionProp(prop4, propX5, propY5, propZ5, currentTime)
            PositionProp(prop5, propX6, propY6, propZ6, currentTime)
            PositionProp(prop6, propX7, propY7, propZ7, currentTime)
            PositionProp(prop7, propX8, propY8, propZ8, currentTime)
            PositionProp(prop8, propX9, propY9, propZ9, currentTime)
            PositionProp(prop9, propX10, propY10, propZ10, currentTime)

        if (index == 2):

            # Position Each Prop
            PositionProp(prop9, propX, propY, propZ, currentTime)
            PositionProp(prop10, propX2, propY2, propZ2, currentTime)
            PositionProp(prop1, propX3, propY3, propZ3, currentTime)
            PositionProp(prop2, propX4, propY4, propZ4, currentTime)
            PositionProp(prop3, propX5, propY5, propZ5, currentTime)
            PositionProp(prop4, propX6, propY6, propZ6, currentTime)
            PositionProp(prop5, propX7, propY7, propZ7, currentTime)
            PositionProp(prop6, propX8, propY8, propZ8, currentTime)
            PositionProp(prop7, propX9, propY9, propZ9, currentTime)
            PositionProp(prop8, propX10, propY10, propZ10, currentTime)

        if (index == 3):

            # Position Each Prop
            PositionProp(prop8, propX, propY, propZ, currentTime)
            PositionProp(prop9, propX2, propY2, propZ2, currentTime)
            PositionProp(prop10, propX3, propY3, propZ3, currentTime)
            PositionProp(prop1, propX4, propY4, propZ4, currentTime)
            PositionProp(prop2, propX5, propY5, propZ5, currentTime)
            PositionProp(prop3, propX6, propY6, propZ6, currentTime)
            PositionProp(prop4, propX7, propY7, propZ7, currentTime)
            PositionProp(prop5, propX8, propY8, propZ8, currentTime)
            PositionProp(prop6, propX9, propY9, propZ9, currentTime)
            PositionProp(prop7, propX10, propY10, propZ10, currentTime)

        if (index == 4):

            # Position Each Prop
            PositionProp(prop7, propX, propY, propZ, currentTime)
            PositionProp(prop8, propX2, propY2, propZ2, currentTime)
            PositionProp(prop9, propX3, propY3, propZ3, currentTime)
            PositionProp(prop10, propX4, propY4, propZ4, currentTime)
            PositionProp(prop1, propX5, propY5, propZ5, currentTime)
            PositionProp(prop2, propX6, propY6, propZ6, currentTime)
            PositionProp(prop3, propX7, propY7, propZ7, currentTime)
            PositionProp(prop4, propX8, propY8, propZ8, currentTime)
            PositionProp(prop5, propX9, propY9, propZ9, currentTime)
            PositionProp(prop6, propX10, propY10, propZ10, currentTime)

        # Move Each Prop Each Loop
        if (index == 5):

            # Position Each Prop
            PositionProp(prop6, propX, propY, propZ, currentTime)
            PositionProp(prop7, propX2, propY2, propZ2, currentTime)
            PositionProp(prop8, propX3, propY3, propZ3, currentTime)
            PositionProp(prop9, propX4, propY4, propZ4, currentTime)
            PositionProp(prop10, propX5, propY5, propZ5, currentTime)
            PositionProp(prop1, propX6, propY6, propZ6, currentTime)
            PositionProp(prop2, propX7, propY7, propZ7, currentTime)
            PositionProp(prop3, propX8, propY8, propZ8, currentTime)
            PositionProp(prop4, propX9, propY9, propZ9, currentTime)
            PositionProp(prop5, propX10, propY10, propZ10, currentTime)

        if (index == 6):

            # Position Each Prop
            PositionProp(prop5, propX, propY, propZ, currentTime)
            PositionProp(prop6, propX2, propY2, propZ2, currentTime)
            PositionProp(prop7, propX3, propY3, propZ3, currentTime)
            PositionProp(prop8, propX4, propY4, propZ4, currentTime)
            PositionProp(prop9, propX5, propY5, propZ5, currentTime)
            PositionProp(prop10, propX6, propY6, propZ6, currentTime)
            PositionProp(prop1, propX7, propY7, propZ7, currentTime)
            PositionProp(prop2, propX8, propY8, propZ8, currentTime)
            PositionProp(prop3, propX9, propY9, propZ9, currentTime)
            PositionProp(prop4, propX10, propY10, propZ10, currentTime)

        if (index == 7):

            # Position Each Prop
            PositionProp(prop4, propX, propY, propZ, currentTime)
            PositionProp(prop5, propX2, propY2, propZ2, currentTime)
            PositionProp(prop6, propX3, propY3, propZ3, currentTime)
            PositionProp(prop7, propX4, propY4, propZ4, currentTime)
            PositionProp(prop8, propX5, propY5, propZ5, currentTime)
            PositionProp(prop9, propX6, propY6, propZ6, currentTime)
            PositionProp(prop10, propX7, propY7, propZ7, currentTime)
            PositionProp(prop1, propX8, propY8, propZ8, currentTime)
            PositionProp(prop2, propX9, propY9, propZ9, currentTime)
            PositionProp(prop3, propX10, propY10, propZ10, currentTime)

        if (index == 8):

            # Position Each Prop
            PositionProp(prop3, propX, propY, propZ, currentTime)
            PositionProp(prop4, propX2, propY2, propZ2, currentTime)
            PositionProp(prop5, propX3, propY3, propZ3, currentTime)
            PositionProp(prop6, propX4, propY4, propZ4, currentTime)
            PositionProp(prop7, propX5, propY5, propZ5, currentTime)
            PositionProp(prop8, propX6, propY6, propZ6, currentTime)
            PositionProp(prop9, propX7, propY7, propZ7, currentTime)
            PositionProp(prop10, propX8, propY8, propZ8, currentTime)
            PositionProp(prop1, propX9, propY9, propZ9, currentTime)
            PositionProp(prop2, propX10, propY10, propZ10, currentTime)

        if (index == 9):

            # Position Each Prop
            PositionProp(prop2, propX, propY, propZ, currentTime)
            PositionProp(prop3, propX2, propY2, propZ2, currentTime)
            PositionProp(prop4, propX3, propY3, propZ3, currentTime)
            PositionProp(prop5, propX4, propY4, propZ4, currentTime)
            PositionProp(prop6, propX5, propY5, propZ5, currentTime)
            PositionProp(prop7, propX6, propY6, propZ6, currentTime)
            PositionProp(prop8, propX7, propY7, propZ7, currentTime)
            PositionProp(prop9, propX8, propY8, propZ8, currentTime)
            PositionProp(prop10, propX9, propY9, propZ9, currentTime)
            PositionProp(prop1, propX10, propY10, propZ10, currentTime)

        # add the current time
        currentTime += interval

        # if we are done
        if (currentTime > endTime):

            # exit while loop
            break

    text_edit.insertPlainText("Your Props Are Ready To Teleport. Press Play." +  "\r\n")

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("Prop Teleportatiion Widget")

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
IntervalSliderLabel = QtWidgets.QLabel("Interval Seconds (1 - 30)")
IntervalSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)

# 1 To 30 Seconds
IntervalSlider.setRange(1, 30)

IntervalSlider.setSingleStep(1)

# Default to 5 Seconds
IntervalSlider.setValue(5)

# Buttons #
TeleportButton = QtWidgets.QPushButton("Teleport Props")
TeleportButton.clicked.connect(TeleportProps)

# Margin Label
marginLabel = QtWidgets.QLabel()


for widget in [text_edit, IntervalSliderLabel, IntervalSlider, marginLabel, TeleportButton]:
    main_widget_layout.addWidget(widget)

dockable_window.Show()