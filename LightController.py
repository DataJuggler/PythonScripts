import RLPy
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance


def TurnOnLights():
    text_edit.clear()
    
    text_edit.insertPlainText("Turning On All Spot Lights..." + "\r\n")
    ActivatedCount = 0
    lightName = "Spot Light"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_SpotLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(True)
        ActivatedCount += 1

    text_edit.insertPlainText("Activated " + str(ActivatedCount) + " Spot Lights." + "\r\n")

    # Reset #
    ActivatedCount = 0

    text_edit.insertPlainText("Turning On All Directional Lights..." + "\r\n")
    lightName = "Dir. Light"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_DirectionalLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(True)
        ActivatedCount += 1

    text_edit.insertPlainText("Activated " + str(ActivatedCount) + " Directional Lights." + "\r\n")

    # Reset #
    ActivatedCount = 0

    text_edit.insertPlainText("Turning On All Point Lights..." + "\r\n")
    
    lightName = "Point light"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_PointLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(True)
        ActivatedCount += 1

    lightName = "Point light(0)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_PointLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(True)
        ActivatedCount += 1

    lightName = "Point light(1)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_PointLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(True)
        ActivatedCount += 1

    lightName = "Point light(2)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_PointLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(True)
        ActivatedCount += 1

    lightName = "Point light(3)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_PointLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(True)
        ActivatedCount += 1

    text_edit.insertPlainText("Activated " + str(ActivatedCount) + " Point Lights." + "\r\n")

      # Reset #
    ActivatedCount = 0

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Show(light)
        ActivatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp2"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Show(light)
        ActivatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp3"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Show(light)
        ActivatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp4"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Show(light)
        ActivatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp5"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Show(light)
        ActivatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp6"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Show(light)
        ActivatedCount += 1

    text_edit.insertPlainText("Showed " + str(ActivatedCount) + " Fluorescent lamps." + "\r\n")

def TurnOffLights():
    text_edit.clear()
    
    text_edit.insertPlainText("Turning Off All Spot Lights..." + "\r\n")
    DeativatedCount = 0
    lightName = "Spot Light"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_SpotLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(False)
        DeativatedCount += 1

    text_edit.insertPlainText("Deactivated " + str(DeativatedCount) + " Spot Lights." + "\r\n")

    text_edit.insertPlainText("Turning Off All Directional Lights..." + "\r\n")

    # Reset #
    DeativatedCount = 0

    lightName = "Dir. Light"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_DirectionalLight,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(False)
        DeativatedCount += 1

    text_edit.insertPlainText("Deactivated " + str(DeativatedCount) + " Directional Lights." + "\r\n")

    # Reset #
    DeativatedCount = 0

    text_edit.insertPlainText("Turning Off All Point Lights..." + "\r\n")

    lightName = "Point light"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Light,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(False)
        DeativatedCount += 1

    lightName = "Point light(0)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Light,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(False)
        DeativatedCount += 1

    lightName = "Point light(1)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Light,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(False)
        DeativatedCount += 1

    lightName = "Point light(2)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Light,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(False)
        DeativatedCount += 1

    lightName = "Point light(3)"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Light,  lightName)

    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        light.SetActive(False)
        DeativatedCount += 1

    text_edit.insertPlainText("Deativated " + str(DeativatedCount) + " Point Lights." + "\r\n")

    # Reset #
    DeativatedCount = 0

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Hide(light)
        DeativatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp2"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Hide(light)
        DeativatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp3"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Hide(light)
        DeativatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp4"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Hide(light)
        DeativatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp5"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Hide(light)
        DeativatedCount += 1

    # now showing the Fluorescent lamps
    lightName = "Fluorescent lamp6"
    all_lights = RLPy.RScene.FindObjects(RLPy.EObjectType_Prop, lightName)
    # Iterate All Props
    for i in range(len(all_lights)):
        light = all_lights[i]
        RLPy.RScene.Hide(light)
        DeativatedCount += 1

    text_edit.insertPlainText("Hid " + str(DeativatedCount) + " Fluorescent lamps." + "\r\n")

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

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)

# Buttons #
TurnOnButton = QtWidgets.QPushButton("Turn On All Lights")
TurnOnButton.clicked.connect(TurnOnLights)

# Buttons #
TurnOffButton = QtWidgets.QPushButton("Turn Off All Lights")
TurnOffButton.clicked.connect(TurnOffLights)

for widget in [progress_bar, text_edit, TurnOnButton, TurnOffButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()