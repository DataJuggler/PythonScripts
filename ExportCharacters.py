import bpy

def ExportCharacter(character, y):

    # Add a TextObject
    bpy.ops.object.text_add(location=(0, y, 0))    

    # change the font if you don't have this font
    bpy.ops.font.open(filepath="C:\\Windows\\Fonts\\Palatino Linotype.TTF", relative_path=True)
            
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
    path = "D:\\3D\\Codopy\\" + name + ".usdc"
    bpy.ops.wm.usd_export(filepath=path, start=1, end=250, selected_objects_only=True, init_scene_frame_range=False)


# text to write
chars = "CODE COPY"

y = -4

for char in chars:
    
    y = y + 1
            
    # export each char
    ExportCharacter(char, y)



    