# PythonScripts
This project contains my ventures in Python for IClone. Please use at your own risk, and if you find something useful let me know.

I am always open to a better way.

Update 11.28.2021:
# Car Driver.py

I created a new script called Car Driver.py. To use this script. create one or more cars, and name them Car1, Car2, etc. Line up a horizontal road, and line up a car where you want cars to start (off screen to the left or right usually). The script is currently only one way, but I will update with two way and more realistic looking traffic as soon as I can.

This part takes some manual configuration in IClone, as I had to edit the Pivot positions of all the cars so that the rotation z and position z are set to 0 in Edit Pivot (which resets Transform values to match). This way all cars point the same direction at 0 rotation, and are the same vertical position.

It works, however I still need to rotate the tires, which also have to all be renamed to:
Car[CarNumber]Wheel[Front|Back][Left|Right]
Examples: (don't use, use what is below starting with Wheel)
Car1WheelFL  - Front Left

Car1WheelFR  - Front Right

Car1WheelRL  - Rear Left

Car1WheelRR  - Rear Right

# Edit 12.3.2021:
The above didn't work, because I had to get the cars starting with car, so I wrote a rename button, and it renamed all the props to:
WheelFLCar1

WheelFRCar1

WheelRLCar1

WheelRRCar1



The current version checked in does not spin the tires, but the other thing you have to do for this to work is detach the tires from the car.
Once the tire spin is implimented, the tires will be rotated depending on the Direction (Left to Right or Right to Left).
After the tires are rotated I plan on reattaching them to the car. As of the time of this writing, you can't get child props from a prop, so that is why
the tires have to be detached.

Some of my cars do not have all 4 sets wheels, as a couple only have 'Read Wheels', so you may see some special cases for if car number == 2 or 9 in my case, I have to switch the prop name to RearWheels. I will try and make this as generic as possible, else if I leave this in by accident, just take it out.


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

