import bpy



class GRAPH_OT_SampleSteps(bpy.types.Operator):
    bl_idname = "graph.sample_steps"
    bl_label = "sample_steps"
    bl_description = "sample steps"

    @classmethod
    def poll(self, context):
        return True

    def get_selected_range(self, fcurv):
        first = None
        last = None
        for point in fcurv.keyframe_points:
            if first == None and point.select_control_point:
                first = point
            elif point.select_control_point:
                last = point
        return (first, last)

    def add_points(self, fcurv, curv_range, step):
        t_min = curv_range[0].co.x
        t_max = curv_range[1].co.x
        nb_points = (t_max - t_min) / step
        evaluated_keys = []
        for i in range(1, int(nb_points) + 1):
            frame = t_min + (i * step)
            evaluated_keys.append((frame, fcurv.evaluate(frame)))
        for key in evaluated_keys:
            fcurv.keyframe_points.insert(frame=key[0], value = key[1])
   
    def update_keyframe_points(self, context):
        """# The select operator(s) are bugged, and can fail to update selected keys, so"""
        area = context.area.type
        if area != 'GRAPH_EDITOR':
            context.area.type = 'GRAPH_EDITOR'

        bpy.ops.transform.transform()

        if area != 'GRAPH_EDITOR':
            context.area.type = area
    
    def execute(self, context):
        self.update_keyframe_points(context)
        #print(context.selected_editable_fcurves)
        #print(context.selected_visible_fcurves)
        for fcurv in context.selected_editable_fcurves:
            points = self.get_selected_range(fcurv)
            if points[0] == None or points[1] == None:
                continue
            self.add_points(fcurv, points, context.scene.sample_step)
            
        return{"FINISHED"}


        