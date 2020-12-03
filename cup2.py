import bpy
# Clear scene
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

## подставка+
#bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
bpy.context.scene.cursor_location = (0.0, 0.0, 0.25)
#bpy.ops.mesh.primitive_cylinder_add(depth=0.5, radius=2.5, 
bpy.ops.mesh.primitive_cylinder_add(depth=0.5, radius=2.4, 
    vertices=360, end_fill_type='NOTHING')
    
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.1
bpy.ops.object.modifier_apply(apply_as='DATA', 
    modifier="Solidify")

## дно +
bpy.context.scene.cursor_location = (0.0, 0.0, 0.5)
bpy.ops.mesh.primitive_circle_add(radius= 2.5, 
    fill_type='TRIFAN') 

## стенки
#bpy.context.scene.cursor_location = (0.0, 0.0, 4.5)
bpy.context.scene.cursor_location = (0.0, 0.0, 4.75)
bpy.ops.mesh.primitive_cone_add(radius2=3.65, radius1=2.5, 
vertices=360, depth=9, end_fill_type='NOTHING')
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.1
bpy.ops.object.modifier_apply(apply_as='DATA', 
    modifier="Solidify")


## закрутка # 0.3 радиус тора 3.65 внутренний радиус 
#bpy.context.scene.cursor_location = (0.0, 0.0, 9.0)
bpy.context.scene.cursor_location = (0.0, 0.0, 9.25)
bpy.ops.mesh.primitive_torus_add(major_radius=3.7,
    major_segments=320, minor_radius=0.15)
    #, abso_major_rad=3.8)


## add camera
from math import pi
#bpy.ops.object.camera_add(view_align=False, location=[0, 10, 30], rotation=[0.436, 0, pi])
bpy.ops.object.camera_add(view_align=False, 
    location=[0, 30, 5], rotation=[1.6, 0, pi])
## add lamp
bpy.ops.object.lamp_add(location=[0,10,18])
bpy.ops.object.lamp_add(location=[0,-10,18])
bpy.ops.object.lamp_add(location=[-10,10,18])
bpy.ops.object.lamp_add(location=[10,10,18])

################################################################

material_obj = bpy.data.materials.new('number_1_material')

imgpath = "/Users/pike/blender/logo.png" 
image_obj = bpy.data.images.load(imgpath)

texture_obj = bpy.data.textures.new('number_1_texture', 
    type='IMAGE')
texture_obj.image = image_obj
texture_obj.extension = 'CLIP'


texture_slot = material_obj.texture_slots.add()

texture_slot.texture = texture_obj
texture_slot.texture_coords = 'OBJECT'
texture_slot.object = bpy.data.objects['Cone']
texture_slot.mapping = 'CUBE'

cone = bpy.data.objects['Cone']
bpy.context.scene.objects.active = cone
bpy.context.scene.objects.active.data.materials.append(material_obj)

#bpy.data.textures["number_1_tex"].use_flip_axis = True
#bpy.data.textures["number_1_tex"].extension = 'CLIP'

bpy.data.objects['Cone'].select = True

#bpy.data.materials['number_1_material'].diffuse_color