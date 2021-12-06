# PythonScripts
This project contains my ventures in Python for IClone. Please use at your own risk, and if you find something useful let me know.

I am always open to a better way.

Update 11.28.2021:
# Car Driver.py

This script requires a lot of manual configuration in IClone. 

Step 1: Add as many cars as you want. Name them Car1, Car2, etc.

Step 2: Run this Python script, and click 'Reposition Cars'.

Step 3: Rename Tires and Detach

This is a pain, but you can't refer to the child objects in IClone's Python API, so you have to rename all your tires and detach them. 
The script does put them back. Here is an example for car 1: 

WheelFLCar1, WheelFRCar1, WheelRLCar1, WheelRRCar1

Renaming Wheels Help

Car[CarNumber]Wheel[Front|Back][Left|Right]
Examples: (don't use, use what is below starting with Wheel)
Car1WheelFL  - Front Left

Car1WheelFR  - Front Right

Car1WheelRL  - Rear Left

Car1WheelRR  - Rear Right

Step 4: Run this script again, click the Reset Pivot button.

Step 5: Make a copy of one of your cars (and delete it later), to get the position where you want cars to start (off screen to the left is what I use for direction 0, and off screen to the right for direction 1. Set the PositionX2, Y2, and Z2 for direction also.

I will include a project with an empty Bowling Alley exterior and Road that has the values in the script to the marketplace when I get a chance, but I can't give away the cars because I didn't buy the export license. 

In IClone, on the Modify > Transform tab, copy the PositionX, Y and Z values from IClone and replace the ones I have in this script (search for
start position and end position comments), if you are not using my Bowling Alley project. 

Step 6: Remove all car animations (all scene animation preferably), and make sure your project is set to the length you want, and that your current time in IClone is Frame 1.

Tip: I have found it takes about 600 - 1200 frames to start showing cars, depending on how far off screen your start positions are, so I made my project 19,200 frames, and rendered from 900, gives over 5 minutes of car traffic. 

Notes:
In addition to the Reset Pivot button, some cars had one rear wheel, so I deleted it and added my own rear wheels (clones of the front wheels).

Some wheels had to be selected, and Middle Center selected as the Pivot, even though it was already saying Middle, this seemed to fix wheels that didn't rotate properly.

Future Plans: It would be nice to have things like traffic comes to a stop in places (for red lights or just traffic). Having a some cars make turns and go in anoteher direction would add realism. Break lights that come on and off would be cool, and head lights that actually light up, but these are version 2 things.

Just happy to be done with this.





Update 2.5.2021: 3D Text Speller
3DSpeller.py    - I do not understand how to publish to the Reallusion Marketplace, so I am giving this away free, so I don't spend any more time trying to make $1.
If you find it useful and want to send me a $1 to help feed my dog, it is always appreciated, but not required. Contact me for how.

the 3D Speller now has a Scale and an option to apply the texture to the glow channel also plus a strength slider. The spacing is also better, but still far from perfect.
The spacing after a comma is a known issue and on my to-do list, but fixing problems that only save a few seconds tend to get very low priority so it might take me 30 minutes or 7 years.

The glow works best usually with not too much glow or it "burns" the image sometimes if that is the right term.

Here is a video demonstrating how to use it: 
https://youtu.be/CljjctTXnGU

Please like and subscribe if you think it is worth the price of free.

If I owe you money after you download and try it, I offer triple your money back, plus a small $1.50 restocking fee.

Let me know if you what you think of the 3D Speller.

Poker Room

Edit 2.25.2021: The Poker Room is coming. I got distracted on shoes, than a 3D Speller, but I am building characters for the Poker Room this weekend.
I would like to have the dealer simulate cards, but that might be a ways off.

The two scripts Scramble and Unscramble will be deleted, but here is a video using them.
https://youtu.be/QytGglxRNLg

Today I learned how to build a graphical user interface so I have a new script called Poker Room Python Widget.

The Shuffle Machine animations now work.

My next possibility is to learn to have a dealer really deal the cards, but it might be over my head to do this yet.

Infinite Road.py
I create a box and apply a road texture, then make 40 copies of the road.
Finally I set the camera up for the 1st and last frames so the camera moves down the road.

To use this script, you must download the file Asphalt With 4 Stripes.png from this repo, and change line 43 of this Python Script to your path:
    image_file = "C:\\Graphics\\Textures\Asphalt With 4 Stripes.png"

This is not infinite yet, it is 40 frames. Baby steps.

Here is a video using it (coming soon):

Let me know if you have any questions. I am very new to Python, but not new in general so I can maybe figure it out.

