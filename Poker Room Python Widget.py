import RLPy
import random
from PySide2 import QtWidgets
from PySide2.shiboken2 import wrapInstance



def RotateChip(chipName, reset = False):
    #-- Loop through props --#prop
    prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, chipName)
    #-- Get Transform Control and Data --#
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()
    rotationValue = 0

    if (reset):
        # set to 0 for reset #
        rotationValue = 0        
    else:
        # create a random value #
        rotationValue = random.randint(101771, 124193) % 89 - 45
        print(rotationValue)        

    #-- Set Rotation Z = by a random amount
    ts_data_block.SetData("Rotation/RotationZ", FrameTime, RLPy.RVariant(rotationValue * RLPy.RMath.CONST_DEG_TO_RAD))
    
def ScrambleRedChips(reset = False):
    
    # Red Chips #
    sum = 0
    n = 82

    propName = "RedChip"
    chipName = ""

    for counter in range(2, n+1):
        if (counter != 51):
            chipName = propName + str(counter)
            print ("attempting to rotate " + chipName)
            
            RotateChip(chipName, reset)
            
            sum += 1

    # show a message #
    if (reset):
        print("Reset " + str(sum) + " Red Chips.");
        text_edit.insertPlainText("Red Chips Unscrambled: " + str(sum) + "\r\n")
    else:
        print("Rotated " + str(sum) + " Red Chips.");
        text_edit.insertPlainText("Red Chips Scrambled: " + str(sum) + "\r\n")
    text_edit.update()

    # return value #
    return sum

def ScrambleBlackChips(reset = False):
    # Black Chips #
    sum = 0
    n = 50

    propName = "BlackChip"
    chipName = ""

    for counter in range(2, n+1):
        chipName = propName + str(counter)
        print ("attempting to rotate " + chipName)
        RotateChip(chipName, reset)
        sum += 1

    # show a message #
    if (reset):
        print("Reset " + str(sum) + " Black Chips.");
        text_edit.insertPlainText("Black Chips Unscrambled: " + str(sum) + "\r\n")
    else:
        print("Rotated " + str(sum) + " Black Chips.");
        text_edit.insertPlainText("Black Chips Scrambled: " + str(sum) + "\r\n")
    text_edit.update()

    # return value #
    return sum

def ScramblePurpleChips(reset = False):
    # Purple Chips #
    sum = 0
    n = 30

    propName = "PurpleChip"
    chipName = ""

    for counter in range(2, n+1):
        chipName = propName + str(counter)
        print ("attempting to rotate " + chipName)
        RotateChip(chipName, reset)
        sum += 1

    # show a message #
    if (reset):
        print("Reset " + str(sum) + " Purple Chips.");
        text_edit.insertPlainText("Purple Chips Unscrambled: " + str(sum) + "\r\n")
    else:
        print("Rotated " + str(sum) + " Purple Chips.");
        text_edit.insertPlainText("Purple Chips Scrambled: " + str(sum) + "\r\n")
    text_edit.update()

    # return value #
    return sum

def ScrambleGoldChips(reset = False):
    # Gold Chips #
    sum = 0
    n = 20

    propName = "GoldChip"
    chipName = ""

    for counter in range(2, n+1):
        chipName = propName + str(counter)
        print ("attempting to rotate " + chipName)
        RotateChip(chipName, reset)
        sum += 1

    # show a message #
    if (reset):
        print("Reset " + str(sum) + " Gold Chips.");
        text_edit.insertPlainText("Gold Chips Unscrambled: " + str(sum) + "\r\n")
    else:
        print("Rotated " + str(sum) + " Gold Chips.");
        text_edit.insertPlainText("Gold Chips Scrambled: " + str(sum) + "\r\n")
    
    text_edit.update()

    # return value #
    return sum

def ScrambleWhiteChips(reset = False):
    # White Chips #
    sum = 0
    n = 50

    propName = "WhiteChip"
    chipName = ""

    for counter in range(2, n+1):
        chipName = propName + str(counter)
        print ("attempting to rotate " + chipName)
        RotateChip(chipName, reset)
        sum += 1

    # show a message #
    if (reset):
        print("Reset " + str(sum) + " White Chips.");
        text_edit.insertPlainText("White Chips Unscrambled: " + str(sum) + "\r\n")
    else:
        print("Rotated " + str(sum) + " White Chips.");
        text_edit.insertPlainText("White Chips Scrambled: " + str(sum) + "\r\n")
    text_edit.update()

    # return value #
    return sum

def ScrambleGreenChips(reset = False):
    # Green Chips #
    sum = 0
    n = 82

    propName = "GreenChip"
    chipName = ""

    for counter in range(2, n+1):
         if (counter != 51):
            chipName = propName + str(counter)
            print ("attempting to rotate " + chipName)
            RotateChip(chipName, reset)
            sum += 1

    # show a message #
    if (reset):
        print("Reset " + str(sum) + " Green Chips.");
        text_edit.insertPlainText("Green Chips Unscrambled: " + str(sum) + "\r\n")
    else:
        print("Rotated " + str(sum) + " Green Chips.");
        text_edit.insertPlainText("Green Chips Scrambled: " + str(sum) + "\r\n")

    text_edit.update()

    # return value #
    return sum

def ScrambleChips():

    FrameTime = RLPy.RGlobal.GetTime()
    text_edit.clear()
    text_edit.update()
    total = 0
    expectedTotal = 306
    progress_bar.setRange(1, expectedTotal)
    # This isn't really 26%, but for some reason the first time it refreshes again this is always behind. #
    progress_bar.setFormat(f"Scrambling: {26}%")
    progress_bar.update()

    total += ScrambleRedChips()

    # Update the progress bar #
    UpdateProgress(total, expectedTotal)

    total += ScrambleBlackChips()

    # Update the progress bar #
    UpdateProgress(total, expectedTotal)
        
    total += ScramblePurpleChips()

    # Update the progress bar #
    UpdateProgress(total, expectedTotal)

    total += ScrambleGoldChips()

    # Update the progress bar #
    UpdateProgress(total, expectedTotal)

    total += ScrambleGreenChips()        

    # Update the progress bar #
    UpdateProgress(total, expectedTotal)

    total += ScrambleWhiteChips()

    # Update the progress bar #
    UpdateProgress(total, expectedTotal)
   
    # Final Message #
    progress_bar.setFormat(f"{total} chips scrambled.")
    progress_bar.update()

    # Refresh Code Hack That Seemed to Work. Waiting For Better Way Answer. #
    Refresh()

def UnscrambleChips():

    FrameTime = RLPy.RGlobal.GetTime()
    text_edit.clear()
    text_edit.update()
    total = 0
    expectedTotal = 306
    progress_bar.setRange(1, expectedTotal)
    # This isn't really 26%, but for some reason the first time it refreshes again this is always behind. #
    progress_bar.setFormat(f"Unscrambling: {26}%")
    progress_bar.update()

    total += ScrambleRedChips(True)

    # Update the progress bar #
    UpdateProgress(total, expectedTotal, True)

    total += ScrambleBlackChips(True)

    # Update the progress bar #
    UpdateProgress(total, expectedTotal, True)

    total += ScramblePurpleChips(True)

    # Update the progress bar #
    UpdateProgress(total, expectedTotal, True)

    total += ScrambleGoldChips(True)

    # Update the progress bar #
    UpdateProgress(total, expectedTotal, True)

    total += ScrambleGreenChips(True)        

    # Update the progress bar #
    UpdateProgress(total, expectedTotal, True)

    total += ScrambleWhiteChips(True)

    # Update the progress bar #
    UpdateProgress(total, expectedTotal, True)
   
    # Final Message #
    progress_bar.setFormat(f"{total} chips unscrambled.")
    progress_bar.update()
    
    # Refresh Code Hack That Seemed to Work. Waiting For Better Way Answer. #
    Refresh()
    
def Refresh():
    
    # Refresh Code Hack That Seemed to Work. Waiting For Better Way Answer. #
    RLPy.RGlobal.Play(RLPy.RTime(FrameTime), RLPy.RTime(FrameTime))
    RLPy.RGlobal.Stop()
    result = RLPy.RGlobal.SetTime(RLPy.RTime(FrameTime))
    print (frameTime)
    result2 = "Set Time Result: "+ result
    print(result2) # Success or fail

def UpdateProgress(progressValue, expectedTotal, reset = False):
    progress_bar.setValue(progressValue)
    if (reset):
        progress_bar.setFormat(f"Unscrambling: {round((progressValue / expectedTotal) * 100)}%")    
    else:
        progress_bar.setFormat(f"Scrambling: {round((progressValue / expectedTotal) * 100)}%")    
    progress_bar.update()

FrameTime = RLPy.RGlobal.GetTime()
window = RLPy.RUi.CreateRDockWidget()
window.SetWindowTitle("Poker Room Python Widget")

dock = wrapInstance(int(window.GetWindow()), QtWidgets.QDockWidget)
dock.setFixedSize(350, 350)
dock.setStyleSheet(
    """ QProgressBar{ font: bold; color: black; border: 1px solid black; background-color: grey;} 
        QProgressBar::chunk { width: 1px; background-color: #13c1ec}""")

widget = QtWidgets.QWidget()
dock.setWidget(widget)

layout = QtWidgets.QVBoxLayout()
widget.setLayout(layout)

progress_bar = QtWidgets.QProgressBar()

text_edit = QtWidgets.QTextEdit(readOnly=True)

ScrambleButton = QtWidgets.QPushButton("Scramble Chips")
ScrambleButton.clicked.connect(ScrambleChips)
UnscrambleButton = QtWidgets.QPushButton("Unscramble Chips")
UnscrambleButton.clicked.connect(UnscrambleChips)

for widget in [progress_bar, text_edit, ScrambleButton, UnscrambleButton]:
    layout.addWidget(widget)

window.Show()