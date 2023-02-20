import bpy
from .register import registerdcr

# ToDo: 'MIX'
# ToDo: 'DARKEN'
# ToDo: 'MUL'
# ToDo: 'COLORBURN'
# ToDo: 'LINEARBURN'
# ToDo: 'LIGHTEN'
# ToDo: 'SCREEN'
# ToDo: 'COLORDODGE'

@registerdcr
class ChangeWPBBmodeToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_add"
    bl_label  = "Change brush blending mode in WP mode to Add"

    def execute(self, context):
         exit_code = change_wp_bbmode("ADD")
         return exit_code

# ToDo: 'OVERLAY'
# ToDo: 'SOFTLIGHT'
# ToDo: 'HARDLIGHT'
# ToDo: 'VIVIDLIGHT'
# ToDo: 'LINEARLIGHT'
# ToDo: 'PINLIGHT'
# ToDo: 'DIFFERENCE'
# ToDo: 'EXCLUSION'
# ToDo: 'SUB'
# ToDo: 'HUE'
# ToDo: 'SATURATION'
# ToDo: 'COLOR'
# ToDo: 'LUMINOSITY'
# ToDo: 'ERASE_ALPHA'
# ToDo: 'ADD_ALPHA'

def change_wp_bbmode(mode):
    try:
        bpy.data.brushes["Draw"].blend = mode
        return {'FINISHED'}
    except Exception as e:
        print(e)
        return { "CANCELLED" }

