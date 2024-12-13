import bpy
import io
import struct
import bmesh
import math
import mathutils
import os

bl_info = {
    "name": "FbxExp Importer (.fbx.bin)",
    "author": "WistfulHopes",
    "version": (1, 0, 0),
    "blender": (4, 3, 0),
    "category": "Import",
}

class CFbxExp_Material:
    def __init__(self, filename, index, textureindex, value):
        self.filename = filename
        self.index = index
        self.textureindex = textureindex
        self.value = value


class CFbxExp_MaterialSection:
    def __init__(self, index = 0, vertexindex = []):
        self.index = index
        self.vertexindex = vertexindex
        

class CFbxExp_Vertex:
    def __init__(self, position = mathutils.Vector(), normal = mathutils.Vector(), color = mathutils.Vector(), uv = mathutils.Vector()):
        self.position = position
        self.normal = normal
        self.color = color
        self.uv = uv


class CFbxExp_Node:
    def __init__(self, type, child, sibling, blendmode = 0, alpha = 0, matrix = mathutils.Matrix(), verts = [], mats = []):
        self.type = type
        self.child = child
        self.sibling = sibling
        self.blendmode = blendmode
        self.alpha = alpha
        self.matrix = matrix
        self.verts = verts
        self.mats = mats

def read_fbxex(context, filepath):
    f = open(filepath, "rb")
    
    f.seek(0x14, 1)
    
    tex_count = struct.unpack('i', f.read(4))[0]
    tex_names = []
    
    for i in range(tex_count):
        tex_names.append(struct.unpack("128s", f.read(0x80))[0].decode().strip())
    
    f.seek(4, 1)
    
    mat_count = struct.unpack('i', f.read(4))[0]
    materials = []
    
    for i in range(mat_count):
        mat_filename = struct.unpack("128s", f.read(0x80))[0].decode().strip()
        mat_index = struct.unpack('i', f.read(4))[0]
        mat_textureindex = struct.unpack('i', f.read(4))[0]
        mat_value = []
        for j in range(17):
            mat_value.append(struct.unpack('i', f.read(4))[0])
        
        materials.append(CFbxExp_Material(mat_filename, mat_index, mat_textureindex, mat_value))    
        
    f.seek(4, 1)
    node_count = struct.unpack('i', f.read(4))[0]
    nodes = []
    
    for i in range(node_count):
        f.seek(4, 1)
        
        node_type = struct.unpack('i', f.read(4))[0]
        node_child = struct.unpack('i', f.read(4))[0]
        node_sibling = struct.unpack('i', f.read(4))[0]
        
        if node_type != 1:
            nodes.append(CFbxExp_Node(node_type, node_child, node_sibling))
        else:
            node_blendmode = struct.unpack('i', f.read(4))[0]
            node_alpha = struct.unpack('f', f.read(4))[0]
            node_matrix = mathutils.Matrix((struct.unpack('ffff', f.read(16)), struct.unpack('ffff', f.read(16)), struct.unpack('ffff', f.read(16)), struct.unpack('ffff', f.read(16))))
            node_matrix.transpose()
            node_vertcount = struct.unpack('i', f.read(4))[0]
            node_verts = []
            
            for j in range(node_vertcount):
                vert_position = mathutils.Vector(struct.unpack('fff', f.read(12)))
                vert_normal = mathutils.Vector(struct.unpack('fff', f.read(12)))
                vert_color = mathutils.Vector(struct.unpack('ffff', f.read(16)))
                vert_uv = mathutils.Vector(struct.unpack('ff', f.read(8)))
                node_verts.append(CFbxExp_Vertex(vert_position, vert_normal, vert_color, vert_uv))

            node_matcount = struct.unpack('i', f.read(4))[0]
            node_mats = []
            
            for j in range(node_matcount):
                node_mat_index = struct.unpack('i', f.read(4))[0]
                vertexindexcount = struct.unpack('i', f.read(4))[0]
                faces = []
                
                for k in range(0, vertexindexcount, 3):
                    faces.append(struct.unpack('iii', f.read(12)))
                
                node_mats.append(CFbxExp_MaterialSection(node_mat_index, faces))
        
            nodes.append(CFbxExp_Node(node_type, node_child, node_sibling, node_blendmode, node_alpha, node_matrix, node_verts, node_mats))
    
    f.close()
    
    parents = {}
    children = {}
    
    for i, node in enumerate(nodes):        
        if node.type != 1:
            next_child = node.child
            next_sibling = node.sibling
            
            bpy.ops.object.empty_add()
            obj = bpy.context.object
            obj.name = "Node_" + str(i)
            
            if (next_child != -1):
                parents[next_child] = bpy.context.object
            
            if (next_sibling != -1):
                children[next_sibling] = bpy.context.object
                
            if i in parents:
                obj.parent = parents[i]
            
            if i in children and children[i].parent is not None:
                obj.parent = children[i].parent

            if i == 0:
                obj.rotation_euler = (1.5707963705062866,0,0)

        else:
            next_child = node.child
            next_sibling = node.sibling
            
            mesh1 = bpy.data.meshes.new("Mesh")
            name = "Node_" + str(i)
            if node.blendmode > 0:
                name += "_Additive"
            if node.alpha > 0:
                name += "_Transparent"
            
            obj = bpy.data.objects.new(name, mesh1)
            bpy.context.collection.objects.link(obj)
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            mesh = bpy.context.object.data
            bm = bmesh.new()
            for v in node.verts:
                bm.verts.new((v.position[0],v.position[1],v.position[2]))
            list = [v for v in bm.verts]
            
            for j, m in enumerate(node.mats):
                material = materials[m.index]
                MeshMat = bpy.data.materials.get(material.filename)
                if not MeshMat:
                    MeshMat = bpy.data.materials.new(material.filename)
                    MeshMat.use_nodes = True
                    
                    if node.blendmode == 0:
                        emission = MeshMat.node_tree.nodes.new('ShaderNodeEmission')
                        texImage = MeshMat.node_tree.nodes.new('ShaderNodeTexImage')
                        texImage.image = bpy.data.images.load(os.path.dirname(filepath) + "\\" + material.filename)
                        mix = MeshMat.node_tree.nodes.new('ShaderNodeMixRGB')
                        mix.blend_type = 'MULTIPLY'
                        attribute = MeshMat.node_tree.nodes.new('ShaderNodeAttribute')
                        attribute.attribute_name = "Color"
                        mix.inputs[0].default_value = 1
                        MeshMat.node_tree.links.new(mix.inputs[1], texImage.outputs['Color'])
                        MeshMat.node_tree.links.new(mix.inputs[2], attribute.outputs['Color'])
                        MeshMat.node_tree.links.new(emission.inputs['Color'], mix.outputs[0])
                        transparent = MeshMat.node_tree.nodes.new('ShaderNodeBsdfTransparent')
                        mix_shader = MeshMat.node_tree.nodes.new('ShaderNodeMixShader')
                        MeshMat.node_tree.links.new(mix_shader.inputs[0], texImage.outputs['Alpha'])
                        MeshMat.node_tree.links.new(mix_shader.inputs[1], transparent.outputs['BSDF'])
                        MeshMat.node_tree.links.new(mix_shader.inputs[2], emission.outputs['Emission'])
                        output = MeshMat.node_tree.nodes["Material Output"]
                        MeshMat.node_tree.links.new(output.inputs[0], mix_shader.outputs['Shader'])
                    else:

                        emission = MeshMat.node_tree.nodes.new('ShaderNodeEmission')
                        texImage = MeshMat.node_tree.nodes.new('ShaderNodeTexImage')
                        texImage.image = bpy.data.images.load(os.path.dirname(filepath) + "\\" + material.filename)
                        mix = MeshMat.node_tree.nodes.new('ShaderNodeMixRGB')
                        mix.blend_type = 'MULTIPLY'
                        attribute = MeshMat.node_tree.nodes.new('ShaderNodeAttribute')
                        attribute.attribute_name = "Color"
                        mix.inputs[0].default_value = 1
                        MeshMat.node_tree.links.new(mix.inputs[1], texImage.outputs['Color'])
                        MeshMat.node_tree.links.new(mix.inputs[2], attribute.outputs['Color'])
                        MeshMat.node_tree.links.new(emission.inputs['Color'], mix.outputs[0])
                        transparent = MeshMat.node_tree.nodes.new('ShaderNodeBsdfTransparent')
                        add_shader = MeshMat.node_tree.nodes.new('ShaderNodeAddShader')
                        MeshMat.node_tree.links.new(add_shader.inputs[0], emission.outputs['Emission'])
                        MeshMat.node_tree.links.new(add_shader.inputs[1], transparent.outputs['BSDF'])
                        output = MeshMat.node_tree.nodes["Material Output"]
                        MeshMat.node_tree.links.new(output.inputs[0], add_shader.outputs['Shader'])
                        MeshMat.blend_method = 'BLEND'
                        
            
                obj.data.materials.append(MeshMat)
                obj.active_material_index = len(obj.material_slots) - 1
        
                for f in m.vertexindex:
                    bm.faces.new((list[f[0]],list[f[1]],list[f[2]]))
                    bm.faces.ensure_lookup_table()
                    f = bm.faces[-1]
                    f.material_index = j
                    if j > 0:
                        print(f.material_index)
                    
            bm.to_mesh(mesh)
            
            uv_layer = bm.loops.layers.uv.verify()
            Normals = []
            for f in bm.faces:
                f.smooth=True
                for l in f.loops:
                    Normals.append(node.verts[l.vert.index].normal)
                    luv = l[uv_layer]
                    try:
                        luv.uv = node.verts[l.vert.index].uv
                    except:
                        continue
            bm.to_mesh(mesh)
            
            color_layer = bm.loops.layers.color.new("Color")
            for f in bm.faces:
                for l in f.loops:
                    l[color_layer]= node.verts[l.vert.index].color
            bm.to_mesh(mesh)
            
            bm.free()

            mesh1.normals_split_custom_set(Normals)
            
            obj.matrix_world = node.matrix
            
            if (next_child != -1):
                parents[next_child] = bpy.context.object
            
            if (next_sibling != -1):
                children[next_sibling] = bpy.context.object
                
            if i in parents:
                obj.parent = parents[i]
            
            if i in children and children[i].parent is not None:
                obj.parent = children[i].parent
            

    return {'FINISHED'}


# ImportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ImportFbxExp(Operator, ImportHelper):
    """An importer for French-Bread's FbxExp model format."""
    bl_idname = "import_scene.fbxex"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "FbxExp (.fbx.bin)"

    # ImportHelper mix-in class uses this.
    filename_ext = ".fbx.bin"

    filter_glob: StringProperty(
        default="*.fbx.bin",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        return read_fbxex(context, self.filepath)


# Only needed if you want to add into a dynamic menu.
def menu_func_import(self, context):
    self.layout.operator(ImportFbxExp.bl_idname, text="FbxExp Importer")


# Register and add to the "file selector" menu (required to use F3 search "Text Import Operator" for quick access).
def register():
    bpy.utils.register_class(ImportFbxExp)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ImportFbxExp)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.import_scene.fbxex('INVOKE_DEFAULT')
