import os, RLPy, math
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance
from PySide2.QtCore import *


def GetCharacterIndex(wordToSpell, character, letterCount):
    index = -1
    tempIndex = -1

    for tempCharacter in wordToSpell:
        tempIndex += 1

        if ((tempIndex < letterCount) and (tempCharacter == character)):
            index += 1

    # return value
    return index

def ApplyMaterialChanged():
    isChecked = applyMaterialCheckBox.isChecked()
    addTextToGlowChannelCheckBox.setVisible(isChecked)
    glowStrengthLabel.setVisible(isChecked)
    glowStrengthSlider.setVisible(isChecked)

def AddTextToGlowChannelChanged():
    isChecked = addTextToGlowChannelCheckBox.isChecked()
    glowStrengthLabel.setVisible(isChecked)
    glowStrengthSlider.setVisible(isChecked)

def SpellWords():

    applyMaterial = False

    if (applyMaterialCheckBox.isChecked()):
        selected = filedialog.exec()
        if selected:
            applyMaterial = True
            materialName = filedialog.selectedFiles()[0]

    text_edit.clear()
    #-- Get iClone 7 default template path --#
    Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    RawKey = OpenKey(Registry, r"SOFTWARE\Reallusion\iClone\7.0")
    ic_template_path = os.path.abspath(QueryValueEx(RawKey, "Template Data" )[0])
    wordSpace = 10
    letterCount = 0
    scaleValue = scaleSlider.value()

    wordToSpell = text_edit2.toPlainText()

    progress_bar.setRange(1, len(wordToSpell))

    fileName = ""
    offSet = 0
    scale = False
    
    text_edit.insertPlainText("Spelling Word " + wordToSpell + ". Please Wait." + "\r\n")

    for character in wordToSpell:
        letterCount += 1

        if (character != " "):
            characterIndex = GetCharacterIndex(wordToSpell, character, letterCount)

            isDigit = character.isdigit()
            if (isDigit):
                propName = "3D_Number_" + character
                fileName = ic_template_path + "//iClone Template//Props//3D_Number_" + character + ".iprop"
            elif (character == "?"):
                propName = "3D_Misc_Question"
                fileName = ic_template_path + "//iClone Template//Props//3D_Misc_Question.iprop"
            elif (character == "="):
                propName = "3D_Math_Equals"
                fileName = ic_template_path + "//iClone Template//Props//3D_Math_Equals.iprop"
                scale = True
            elif (character == "-"):
                propName = "3D_Math_Minus"
                fileName = ic_template_path + "//iClone Template//Props//3D_Math_Minus.iprop"
            elif (character == "+"):
                propName = "3D_Math_Plus"
                fileName = ic_template_path + "//iClone Template//Props//3D_Math_Plus.iprop"
            elif (character == "@"):
                propName = "3D_Misc_At"
                fileName = ic_template_path + "//iClone Template//Props//3D_Misc_At.iprop"
                offSet -= .8
            elif (character == "@"):
                propName = "3D_Misc_At"
                fileName = ic_template_path + "//iClone Template//Props//3D_Misc_At.iprop"
            elif (character == ","):
                propName = "3D_Misc_Comma"
                fileName = ic_template_path + "//iClone Template//Props//3D_Misc_Comma.iprop"
                scale = True
            elif (character == "!"):
                propName = "3D_Misc_Exclamation"
                fileName = ic_template_path + "//iClone Template//Props//3D_Misc_Exclamation.iprop"
            elif (character == "#"):
                propName = "3D_Misc_Hash"
                fileName = ic_template_path + "//iClone Template//Props//3D_Misc_Hash.iprop"
            elif (character == "."):
                propName = "3D_Misc_Period"
                fileName = ic_template_path + "//iClone Template//Props//3D_Misc_Period.iprop"
                offSet += .25
                scale = True
            else:
                propName = "3D_Letter_" + character.upper()
                fileName = ic_template_path + "//iClone Template//Props//3D_Letter_" + character.upper() + ".iprop"
    
            # every instance after the first will be prop(0), prop(1), etc.
            if (characterIndex > 0):
                propName += "(" + str(characterIndex - 1) + ")"

            text_edit.insertPlainText(propName + "\r\n")

            #-- Load iProp --#
            prop = RLPy.RFileIO.LoadObject(fileName)

            ts_control = prop.GetControl("Transform")
            ts_data_block = ts_control.GetDataBlock()

            ts_data_block.SetData("Position/PositionX", RLPy.RTime(0), RLPy.RVariant((letterCount - 1 - offSet) * wordSpace * scaleValue))

            # Scale can only be turned on here, not turned off if already on.
            if (scale == False):
                # if the scaleValue has been changed, all props need to be scaled.
                scale = (scaleValue != 1)

            # if scale is true
            if (scale):
                # safeguard
                if (scaleValue < .5):
                    scaleValue = .5

                # this prop must be scaled
                ts_data_block.SetData("Scale/ScaleX", RLPy.RTime(0), RLPy.RVariant(scaleValue))
                ts_data_block.SetData("Scale/ScaleY", RLPy.RTime(0), RLPy.RVariant(scaleValue))
                ts_data_block.SetData("Scale/ScaleZ", RLPy.RTime(0), RLPy.RVariant(scaleValue))

            # increase by another .5 for the next words
            if (character.upper() == "I"):
                offSet += .5
            elif (character.upper() == "J"):
                offSet += .25
            elif (character.upper() == "M"):
                offSet -= .2
            elif (character.upper() == "W"):
                offSet -= .5
            elif (character.upper() == "O"):
                offSet -= .16
            elif (character.upper() == "A"):
                offSet -= .2
            elif (character.upper() == "G"):
                offSet -= .25
            elif (character.upper() == "C"):
                offSet -= .16

            if (applyMaterial):
                # apply material
                material_component = prop.GetMaterialComponent()
                mesh_list = prop.GetMeshNames()
                mesh_name = mesh_list[0]
                material_list = material_component.GetMaterialNames(mesh_name)
                material_name = material_list[0]
                #Load image to material channel
                texture_channel = RLPy.EMaterialTextureChannel_Diffuse
            
                result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, materialName)

                if (addTextToGlowChannelCheckBox.isChecked()):
                    texture_channel = RLPy.EMaterialTextureChannel_Glow
                    key = RLPy.RKey()
                    key.SetTime(RLPy.RTime(0))
                    diffuse_weight = glowStrengthSlider.value() * .01
                    result = material_component.LoadImageToTexture(mesh_name, material_name, texture_channel, materialName)
                    material_component.AddTextureWeightKey(key, mesh_name, material_name,
                                       texture_channel, diffuse_weight)

        progress_bar.setValue(letterCount)

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("3D Text Speller")

# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()),
                    QtWidgets.QDockWidget)

dock.setFixedSize(640, 640)

main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)
textToSpellLabel = QtWidgets.QLabel("Enter Text To Spell")

text_edit2 = QtWidgets.QTextEdit(readOnly=False)

# scale
scaleLabel = QtWidgets.QLabel("Scale")
scaleSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)
scaleSlider.setRange(.5, 10)
scaleSlider.setSingleStep(.1)
scaleSlider.setValue(1)

applyMaterialCheckBox = QtWidgets.QCheckBox("Browse For Material")
applyMaterialCheckBox.setChecked(True)
applyMaterialCheckBox.stateChanged.connect(ApplyMaterialChanged)

# checkbox and slider for Glow Channel Strength
addTextToGlowChannelCheckBox = QtWidgets.QCheckBox("Add Texture To Glow Channel")
addTextToGlowChannelCheckBox.stateChanged.connect(AddTextToGlowChannelChanged)
glowStrengthLabel = QtWidgets.QLabel("Glow Strength")
glowStrengthSlider = QtWidgets.QSlider(orientation=Qt.Horizontal)
glowStrengthSlider.setRange(1, 100)
glowStrengthSlider.setSingleStep(10)
glowStrengthSlider.setValue(50)

# hide both by default
glowStrengthLabel.setVisible(False)
glowStrengthSlider.setVisible(False)

filedialog = QtWidgets.QFileDialog()
filedialog.setNameFilters(["Images (*.png *.jpg)"])

# Buttons #
SpellWordsButton = QtWidgets.QPushButton("Spell")
SpellWordsButton.clicked.connect(SpellWords)

# Margin Label
marginLabel = QtWidgets.QLabel("")

for widget in [progress_bar, textToSpellLabel, text_edit2, text_edit, scaleLabel, scaleSlider, applyMaterialCheckBox, addTextToGlowChannelCheckBox, glowStrengthLabel, glowStrengthSlider, marginLabel, SpellWordsButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()