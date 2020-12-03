import bpy,bmesh
# Clear scene
def clear():
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def mode(mode_name):
    bpy.ops.object.mode_set(mode=mode_name)
    if mode_name == "EDIT":
        bpy.ops.mesh.select_all(action="DESELECT")
        
clear()
        
## подставка+
#bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
bpy.context.scene.cursor_location = (0.0, 0.0, 0.25)
#bpy.ops.mesh.primitive_cylinder_add(depth=0.5, radius=2.5, 
bpy.ops.mesh.primitive_cylinder_add(depth=0.5, radius=2.4, 
    vertices=360, end_fill_type='NOTHING')

# утолщение    
#bpy.ops.object.modifier_add(type='SOLIDIFY')
#bpy.context.object.modifiers["Solidify"].thickness = 0.1
#bpy.ops.object.modifier_apply(apply_as='DATA', 
#    modifier="Solidify")

## дно +
bpy.context.scene.cursor_location = (0.0, 0.0, 0.5)
bpy.ops.mesh.primitive_circle_add(radius= 2.5, 
    fill_type='TRIFAN') 

## стенки
#bpy.context.scene.cursor_location = (0.0, 0.0, 4.5)
bpy.context.scene.cursor_location = (0.0, 0.0, 4.75)
bpy.ops.mesh.primitive_cone_add(radius2=3.65, radius1=2.5, 
vertices=360, depth=9, end_fill_type='NOTHING')

# утолщение    
#bpy.ops.object.modifier_add(type='SOLIDIFY')
#bpy.context.object.modifiers["Solidify"].thickness = 0.1
#bpy.ops.object.modifier_apply(apply_as='DATA', 
#    modifier="Solidify")


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
    location=[0, -30, 5], rotation=[1.55, 0, 0])
## add lamp
bpy.ops.object.lamp_add(location=[0,10,8])
bpy.ops.object.lamp_add(location=[0,-10,8])
bpy.ops.object.lamp_add(location=[-10,10,8])
bpy.ops.object.lamp_add(location=[10,10,8])

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

# add material to cone
bpy.context.scene.objects.active.data.materials.append(material_obj)

#bpy.data.textures["number_1_tex"].use_flip_axis = True
#bpy.data.textures["number_1_tex"].extension = 'CLIP'

#####################################################
bpy.context.tool_settings.mesh_select_mode = (False, True, False) 

bpy.data.objects['Cone'].select = True

#bpy.context.scene.objects.active = cone

mode('EDIT')
bpy.ops.mesh.select_all(action='DESELECT')

#! bpy.ops.mesh.mark_seam(clear=False)
bpy.ops.mesh.select_mode(type = "EDGE")
# bpy.data.objects['Cone'].select = True

#bm = bmesh.from_edit_mesh(bpy.context.object['Cone'].data)
#bm.edges[7].select = True

#obj = bpy.context.scene.objects.active
#bm  = bmesh.new()
#bm  = bmesh.from_edit_mesh(obj.data)

#bpy.data.materials['number_1_material'].diffuse_color
#print(bm)

#bm.edges[1].select = True

# ok
obj = bpy.context.active_object
bm = bmesh.from_edit_mesh(obj.data)

#for edge in bm.edges:
#    if edge.index % 2 == 0:
#        edge.select = True
#        continue
#    
#    edge.select = False
bm.edges.ensure_lookup_table()    
bm.edges[1].select = True    
bpy.ops.mesh.mark_seam() 


for edge in bm.edges:
#    if edge.index % 2 == 0:
    edge.select = True
#        continue
#    




