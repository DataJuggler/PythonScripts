import os, RLPy, math
from winreg import *
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance


def GetCharacterIndex(wordToSpell, character, letterCount):
    index = -1
    tempIndex = -1

    for tempCharacter in wordToSpell:
        tempIndex += 1

        if ((tempIndex < letterCount) and (tempCharacter == character)):
            index += 1

    # return value
    return index

def SpellWords():
    text_edit.clear()

    #-- Get iClone 7 default template path --#
    Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    RawKey = OpenKey(Registry, r"SOFTWARE\Reallusion\iClone\7.0")
    ic_template_path = os.path.abspath(QueryValueEx(RawKey, "Template Data" )[0])
    wordSpace = 10
    letterCount = 0

    wordToSpell = text_edit2.toPlainText()
    
    text_edit.insertPlainText("Spelling Word " + wordToSpell + ". Please Wait." + "\r\n")

    for character in wordToSpell:
        letterCount += 1

        if (character != " "):
            characterIndex = GetCharacterIndex(wordToSpell, character, letterCount)
            fileName = ic_template_path + "//iClone Template//Props//3D_Letter_" + character.upper() + ".iprop"

            if (characterIndex > 0):
                propName = "3D_Letter_" + character.upper() + "(" + str(characterIndex - 1) + ")"                
            else:
                propName = "3D_Letter_" + character.upper()

            text_edit.insertPlainText(propName + "\r\n")

            #-- Load iProp --#
            RLPy.RFileIO.LoadFile(fileName)

            #-- Get Prop --#
            prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, propName)
    
            ts_control = prop.GetControl("Transform")
            ts_data_block = ts_control.GetDataBlock()

            ts_data_block.SetData("Position/PositionX", RLPy.RTime(0), RLPy.RVariant((letterCount - 1) * wordSpace))
        
    

# Create an iClone Dock Widget
dockable_window = RLPy.RUi.CreateRDockWidget()
dockable_window.SetWindowTitle("3D Text Speller")
# Use wrapInstance to convert the dockable window to something that Python can understand, in this case a Dock Widget
dock = wrapInstance(int(dockable_window.GetWindow()),
                    QtWidgets.QDockWidget)
dock.setFixedSize(640, 480)
main_widget = QtWidgets.QWidget()
dock.setWidget(main_widget)

main_widget_layout = QtWidgets.QVBoxLayout()
main_widget.setLayout(main_widget_layout)

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)

text_edit2 = QtWidgets.QTextEdit(readOnly=False)


# Buttons #
SpellWordsButton = QtWidgets.QPushButton("Spell")
SpellWordsButton.clicked.connect(SpellWords)

for widget in [progress_bar, text_edit2, text_edit, SpellWordsButton]:
    main_widget_layout.addWidget(widget)


dockable_window.Show()