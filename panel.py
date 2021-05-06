import bpy

class GRAPH_PT_SampleStepsPanel(bpy.types.Panel):
    bl_label = "Sample keyframe"
    bl_region_type = 'UI'
    bl_space_type = 'GRAPH_EDITOR'
    bl_category = 'Key'


    @classmethod
    def poll(self, context):
        return True


    def draw(self, context):
        layout = self.layout.row()
        layout.prop(context.scene, 'sample_step', text = 'step')
        layout.operator('graph.sample_steps', text = 'make sample')
