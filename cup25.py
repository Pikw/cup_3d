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

###################################

def set_uvs(mesh, name=None):
    
#    if name is None:
#        if 0<len(mesh.uv_textures):
#            uv = mesh.uv_textures[0]
#        else:
#            uv = mesh.uv_textures.new("cubic")
#    else:
#        uv = mesh.uv_textures.get(name)
#        if uv is None:
#            uv = mesh.uv_textures.new(name)
            
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.faces.ensure_lookup_table()
    
    uv_layer = bm.loops.layers.uv[uv.name]
    
    for fi in range(len(bm.faces)):
        set_uvs_for_face(bm, fi, uv_layer)
    
    bm.to_mesh(mesh)


######################################

def set_UV_editor_texture(mesh):
    """ set the image for the face.tex layer on all the faces
    so we have a rough idea of what the mesh will look like
    in the 3D view's Texture render mode"""

    # load the mesh data into a bmesh object
    bm = bmesh.new()
    bm.from_mesh(mesh)

    bm.faces.ensure_lookup_table()

    # Get the "tex" layer for the first UV map
    # If you don't already have a UV map, why are you even calling this function?
    tex_layer = bm.faces.layers.tex[mesh.uv_layers[0].name]

    for i in range(len(bm.faces)):

        # figure out which material this face uses
        mi = bm.faces[i].material_index
        mat = mesh.materials[mi]

        # Assume that we want to use the image from the first texture slot;
        # and assume that the material has a texture in that first slot;
        # and assume that the texture is an image texture instead of a procedural texture.
        # if any of several assumptions are wrong, this will explode
        img = mat.texture_slots[0].texture.image

        bm.faces[i][tex_layer].image = img

    # copy the modified data into the mesh
    bm.to_mesh(mesh)
    
###################################
        
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
material_obj.use_nodes = True

#imgpath = "/Users/pike/blender/trans.png" 
#image_obj = bpy.data.images.load(imgpath)

texture_obj = bpy.data.textures.new('number_1_texture', 
    type='IMAGE')
#texture_obj.image = image_obj
#texture_obj.extension = 'CLIP'


texture_slot = material_obj.texture_slots.add()

texture_slot.texture = texture_obj
texture_slot.texture_coords = 'UV'
#texture_slot.object = bpy.data.objects['Cone']
#texture_slot.mapping = 'CUBE'
texture_slot.uv_layer = 'default'

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

#bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.mesh.select_all(action= 'SELECT')
bpy.ops.uv.unwrap(method='CONFORMAL', margin=0.001)

#bpy.ops.uv.unwrap(method='CONFORMAL', margin=0.001)

#bpy.ops.image.open(filepath="/Users/pike/blender/trans.png", directory="/Users/pike/blender/", files=[{"name":"trans.png", "name":"trans.png"}], show_multiview=False)
bpy.ops.image.open(filepath="/Users/pike/blender/trans.png", directory="/Users/pike/blender/", files=[{"name":"trans.png"}], show_multiview=False)

#bpy.ops.transform.resize(value=(3.36703, 3.36703, 3.36703), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='CONSTANT', proportional_size=1)
bpy.ops.uv.cursor_set(location=(0.531286, -0.0180997))
#bpy.ops.transform.resize(value=(1.35524, 1.35524, 1.35524), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

bpy.ops.transform.resize(value=(3.00782, 3.00782, 3.00782), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    
#for edge in bm.edges:
#    if edge.index % 2 == 0:
#    edge.select = True
#        continue
#    

#set_UV_editor_texture(obj.data)

#set_uvs(bm)

