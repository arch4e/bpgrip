import bpy

from ..utils.register import registerdcr


@registerdcr
class SetBBmode(bpy.types.Operator):
    bl_idname = 'bpgrip.set_bbmode'
    bl_label  = 'Set brush blending mode'

    bl_mode: bpy.props.StringProperty()
    bb_mode: bpy.props.StringProperty()

    def execute(self, context):
        try:
            bpy.data.brushes[self.bl_mode].blend = self.bb_mode
            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { 'CANCELLED' }

