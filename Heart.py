import bpy


# add a cube
bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# make cube wider
bpy.context.object.scale[1] = 2

# move up
bpy.context.object.location[2] = 1

# add initial cube
bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# scale to make it less thick
bpy.context.object.scale[0] = 0.1

# rotate 45 degrees
bpy.context.object.rotation_euler[0] = 0.785398
# add modifier

# add boolean modifier to be more specific
bpy.ops.object.modifier_add(type='BOOLEAN')

# set the cut cube
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cube"]

# apply modifier
bpy.ops.object.modifier_apply(modifier="Boolean")


# Deselect the second cube
bpy.data.objects['Cube.001'].select_set(False)

# Select the first cube
bpy.data.objects['Cube'].select_set(True)

# delete first cube
bpy.ops.object.delete(use_global=False, confirm=False)

# now create the left cylinder
bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(.8, .8, 1))

# rotate on y axix 90 degrees
bpy.context.object.rotation_euler[1] = 1.5708



# scale the cylinder depth on the z axis
bpy.context.object.scale[2] = 0.1

# align left
bpy.context.object.location[1] = -.8

# move up a little
bpy.context.object.location[2] = 0.51

# now create the left cylinder
bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(.8, .8, .1))

# rotate on y axix 90 degrees
bpy.context.object.rotation_euler[1] = 1.5708

# align right
bpy.context.object.location[1] = .8

# move up a little
bpy.context.object.location[2] = 0.51

# now create the left cylinder
bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(.5, .5, .1))

# rotate on y axix 90 degrees
bpy.context.object.rotation_euler[1] = 1.5708

# now select all objects
for obj in bpy.data.collections['Collection'].all_objects:
    obj.select_set(True)

# join
bpy.ops.object.join()


for obj in bpy.context.selected_objects:
    obj.name = "Heart"
    

# now smooth it out
bpy.context.object.data.use_auto_smooth = True
bpy.ops.object.shade_smooth(use_auto_smooth=True)







