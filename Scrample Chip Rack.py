import RLPy
import random

  

def RotateChip(chipName):
    #-- Loop through props --#prop
    prop = RLPy.RScene.FindObject(RLPy.EObjectType_Prop, chipName)
    #-- Get Transform Control and Data --#
    ts_control = prop.GetControl("Transform")
    ts_data_block = ts_control.GetDataBlock()
    # hard coded for now #
    randomValue = random.randint(101771, 124193) % 59 - 29;
    print(randomValue)
    #-- Set Rotation Z = by a random amount
    ts_data_block.SetData("Rotation/RotationZ", RLPy.RTime(0), RLPy.RVariant(randomValue * RLPy.RMath.CONST_DEG_TO_RAD))


# Red Chips #
sum = 0
n = 82

propName = "RedChip"
chipName = ""

for counter in range(2, n+1):
    if (counter != 51):
        chipName = propName + str(counter)
        print ("attempting to rotate " + chipName)
        RotateChip(chipName)
        sum += 1

# show a message #
print("Rotated " + str(sum) + " Red Chips.");

# Black Chips #
sum = 0
n = 50

propName = "BlackChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to rotate " + chipName)
    RotateChip(chipName)
    sum += 1

# show a message #
print("Rotated " + str(sum) + " Black Chips.");

# Purple Chips #
sum = 0
n = 30

propName = "PurpleChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to rotate " + chipName)
    RotateChip(chipName)
    sum += 1

# show a message #
print("Rotated " + str(sum) + " Purple Chips.");

# Gold Chips #
sum = 0
n = 20

propName = "GoldChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to rotate " + chipName)
    RotateChip(chipName)
    sum += 1

# show a message #
print("Rotated " + str(sum) + " Gold Chips.");

# White Chips #
sum = 0
n = 50

propName = "WhiteChip"
chipName = ""

for counter in range(2, n+1):
    chipName = propName + str(counter)
    print ("attempting to rotate " + chipName)
    RotateChip(chipName)
    sum += 1

# show a message #
print("Rotated " + str(sum) + " White Chips.");

# Green Chips #
sum = 0
n = 82

propName = "GreenChip"
chipName = ""

for counter in range(2, n+1):
     if (counter != 51):
        chipName = propName + str(counter)
        print ("attempting to rotate " + chipName)
        RotateChip(chipName)
        sum += 1

# show a message #
print("Rotated " + str(sum) + " Green Chips.");