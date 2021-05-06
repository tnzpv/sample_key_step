import bpy
from . import panel, operators

bl_info = {
    "name": "Sample steps",
    "author": "Arnaud Flores",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "description": "sample steps",
    "category": "GraphEditor"
    }

classes = (panel.GRAPH_PT_SampleStepsPanel, operators.GRAPH_OT_SampleSteps)

def register():
    bpy.types.Scene.sample_step = bpy.props.IntProperty(default = 1, min = 1)

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.sample_step
    for cls in classes:
        bpy.utils.unregister_class(cls)