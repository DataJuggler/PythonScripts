import RLPy
import random

  

def ResetChip(chipName):
    #-- Loop through props --#prop
    prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, chipName)
    #-- Get Transform Control and Data --#
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()
    # reset back to 0
    resetValue = 0
    #-- Set Rotation Z = 20 degree --#
    ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(0), RLPy.RVariant(resetValue * RLPy.RMath.CONST_DEG_TO_RAD))


# Red Chips #
sum = 0
n = 82

propName = "RedChip"
chipName = ""

for counter in range(2,n+1):

    if (counter != 51):
        chipName = propName + str(counter)
        print ("attempting to reset " + chipName)
        ResetChip(chipName)
        sum += 1

# show a message #
print("Reset " + str(sum) + " Red Chips.");

# Black Chips #
sum = 0
n = 50

propName = "BlackChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to reset " + chipName)
    ResetChip(chipName)
    sum += 1

# show a message #
print("Reset " + str(sum) + " Black Chips.");

# Purple Chips #
sum = 0
n = 30

propName = "PurpleChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to reset " + chipName)
    ResetChip(chipName)
    sum += 1

# show a message #
print("Reset " + str(sum) + " Purple Chips.");


# Gold Chips #
sum = 0
n = 20

propName = "GoldChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to reset " + chipName)
    ResetChip(chipName)
    sum += 1

# show a message #
print("Reset " + str(sum) + " Gold Chips.");

# White Chips #
sum = 0
n = 50

propName = "WhiteChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to reset " + chipName)
    ResetChip(chipName)
    sum += 1

# show a message #
print("Reset " + str(sum) + " White Chips.");

# Green Chips #
sum = 0
n = 82

propName = "GreenChip"
chipName = ""

for counter in range(2, n+1):
    if (counter != 51):
        chipName = propName + str(counter)
        print ("attempting to reset " + chipName)
        ResetChip(chipName)
        sum += 1

# show a message #
print("Reset " + str(sum) + " Green Chips.");

