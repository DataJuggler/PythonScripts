import RLPy
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance


def RenameProps():
    text_edit.clear()
    sourcePropName = str(combo_box.currentText())
    text_edit.insertPlainText("Renaming props starting with: " + sourcePropName + "\r\n")
    RenamedCount = 0
    
    # Iterate All Props
    for i in range(len(all_props)):
        name = all_props[i].GetName()

        if (name != sourcePropName):
            if (sourcePropName in name):
                RenamedCount += 1
                newName = sourcePropName + str(RenamedCount + 1)
                prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, name)
                prop.SetName(newName)
                text_edit.insertPlainText("Renamed props : " + name + " to " + newName + "\r\n")

    text_edit.insertPlainText("Renamed " + str(RenamedCount) + " props." + "\r\n")

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
RenameButton = QtWidgets.QPushButton("Rename Props")
RenameButton.clicked.connect(RenameProps)

for widget in [progress_bar, text_edit, RenameButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()
