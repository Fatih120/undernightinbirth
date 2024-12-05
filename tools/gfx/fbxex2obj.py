# lazy FBX to INDIVIDUAL MODEL/NODE obj files for use in blender
# Use this to extract stages from /bg/ into a model format. WIP for mesh materials.

import json
import numpy as np
import sys
import os

def process_node(node, nodes, matrix=np.eye(4)):
    vertices = []
    faces = []
    
    if isinstance(node, dict):
        if 'matrix' in node:
            node_matrix = np.array(node['matrix']).reshape(4, 4).T
            matrix = np.dot(matrix, node_matrix)
        
        if 'vertex' in node:
            for i in range(node['vertex']['count']):
                v = node['vertex'][str(i)][:3]
                v_homogeneous = np.array([v[0], v[1], v[2], 1])
                v_transformed = np.dot(matrix, v_homogeneous)[:3]
                vertices.append(v_transformed)
            
            if 'material' in node:
                for material in node['material'].values():
                    if isinstance(material, dict) and 'vertexindex' in material:
                        for i in range(0, len(material['vertexindex']), 3):
                            face = [material['vertexindex'][i],
                                    material['vertexindex'][i+1],
                                    material['vertexindex'][i+2]]
                            faces.append(face)
    
    return vertices, faces

def save_obj(vertices, faces, filename):
    with open(filename, 'w') as f:
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for face in faces:
            f.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")

def process_file(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    nodes = data['fbxex']['node']

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_dir = f"{base_name}_obj"
    os.makedirs(output_dir, exist_ok=True)

    for node_id, node in nodes.items():
        vertices, faces = process_node(node, nodes)
        
        if vertices and faces:
            output_file = os.path.join(output_dir, f"{base_name}_{node_id}.obj")
            save_obj(vertices, faces, output_file)
            print(f"extracted {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Drag-drop or pass a bg.fbx.json to extract.")
        input("Press Enter to exit.")
    else:
        for file_path in sys.argv[1:]:
            if file_path.lower().endswith('.json'):
                process_file(file_path)
            else:
                print(f"Not a JSON file.")
        
        input("Press Enter to exit.")
