import bpy


Number = 0

for n in range(1, 11):
    for i in range(1, 11):
    
        y = -10 + (i * 2)
        z = 10 - (n * 2)
        
        if ((i < 11) and (n < 11)):
            Number = Number + 1
        
        bpy.ops.object.text_add(location=(0, y, z))    
        bpy.ops.font.open(filepath="C:\\Windows\\Fonts\\ARLRDBD.TTF", relative_path=True)
        # text_object = bpy.context.object
        # text_object.data.body = str(i)
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')

        


        # if a linebreak is needed
        # bpy.ops.font.line_break()

        
        
        chars = str(Number)
        
        
        
        for char in chars:
            
            bpy.ops.font.text_insert(text=char)   
            
            
            
        bpy.ops.object.editmode_toggle()
        
        bpy.context.object.data.extrude = 0.06

        bpy.context.object.name = "Number" + str(Number)

        # for obj in bpy.context.selected_objects:
        # Number  obj.name = "Number" + str(Number)

        # rotate 
        bpy.context.object.rotation_euler[0] = 1.5708
        bpy.context.object.rotation_euler[2] = 1.5708


    



    