import RLPy
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance


def DuplicateProp():
    text_edit.clear()
    sourcePropName = str(combo_box.currentText())
    text_edit.insertPlainText("Duplicating prop: " + sourcePropName + "\r\n")
    DuplicatetedCount = 0

    numberToDuplicate = 12
    SourceY = -4564
    SecondRowX = 1512

    SecondRow = False
    increment = 960

    # Iterate All Props
    for i in range(1, numberToDuplicate):

        SecondRow = (i % 2 == 1)
        
        newName = sourcePropName + str(i)
        prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, sourcePropName)
        DuplicatetedCount += 1
        newName = sourcePropName + str(DuplicatetedCount + 1)
        clonedProp = prop.Clone()
        clonedProp.SetName(newName)

        #-- Set Position X = 100 --#
        ts_control = clonedProp.GetControl("Transform")
        moveAmount = SourceY + (increment * DuplicatetedCount)
        ts_data_block = ts_control.GetDataBlock()

        if (SecondRow):
            moveAmount -= 480
            ts_data_block.SetData("Position/PositionX", RLPy.RTime(0), RLPy.RVariant(SecondRowX))        

        #-- Set Position X = 100 --#        
        ts_data_block.SetData("Position/PositionY", RLPy.RTime(0), RLPy.RVariant(moveAmount))

        text_edit.insertPlainText("Replicated prop : " + sourcePropName + " as " + newName + "\r\n")

    text_edit.insertPlainText("Replicated " + str(DuplicatetedCount) + " props." + "\r\n")

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("All Scene Props")
# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()),
                    QtWidgets.QDockWidget)
dock.setFixedSize(640, 480)
main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

combo_box = QtWidgets.QComboBox()

main_widget_layout.addWidget(combo_box)

# Grab all props in the scene
all_props = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop)
# Add an entry into the combo-box for every prop found
for i in range(len(all_props)):
    combo_box.addItem(all_props[i].GetName())

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)

# Buttons #
DuplicateButton = QtWidgets.QPushButton("Duplicate Prop")
DuplicateButton.clicked.connect(DuplicateProp)

for widget in [progress_bar, text_edit, DuplicateButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()
