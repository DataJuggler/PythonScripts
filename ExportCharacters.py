# This file is used to export text one character at a time from Blender
# To use it, you must change:
# 1. Line 53 - The folder path to path=[drive]:\\YourFolder\\YourSubFolder (don't forget Python uses double backslash \\ for direcrtory separator)
#    example: D:\\3D\\BlenderCharacters
# 2. Line 58 - The text to create to chars = "YOUR TEXT"
# 3. Line 20 - Change the font path to a path you have (It is on my to do list to learn how to build Add On GUI's)

import bpy

def ExportCharacter(character, y):

    # Add a TextObject
    bpy.ops.object.text_add(location=(0, y, 0))    

    # change the font if you don't have this font
    # On Windows, your fonts are located in c:\Windows\Fonts, make sure you have the font used
    # Also do not forget that the font path must use double backslash \\ for each directory
    
    # Font I Use In The Video
    # bpy.ops.font.open(filepath="C:\\Windows\\Fonts\\Palatino Linotype.TTF", relative_path=True)
    
    # Font Verdana - Every Windows Machine Should Have This
    bpy.ops.font.open(filepath="C:\\Windows\\Fonts\\Verdana.TTF", relative_path=True)
            
    # go into edit mode and delete existing characters TEXT
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')

    char = character
    bpy.ops.font.text_insert(text=char)   
                
    # exit edit mode            
    bpy.ops.object.editmode_toggle()
            
    # set extrude
    bpy.context.object.data.extrude = 0.06

    # set the name of this character
    name = "Letter" + character
    bpy.context.object.name = name

    # rotate 
    bpy.context.object.rotation_euler[0] = 1.5708
    bpy.context.object.rotation_euler[2] = 1.5708

    # helps with export
    bpy.ops.object.modifier_add(type='TRIANGULATE')

    # export change the path to save to
    path = "C:\\Temp" + name + ".usdc"
    bpy.ops.wm.usd_export(filepath=path, start=1, end=250, selected_objects_only=True, init_scene_frame_range=False)



# text to write
chars = "CODE COPY"

y = -3.6

for char in chars:
    
    y = y + .75
            
    if not char.isspace():

        # export each char
        ExportCharacter(char, y)
    
    else:
        
        # go back a little
        y = y -.5



    
