import bpy
from .register import registerdcr

@registerdcr
class ChangeWPBBmodeToMix(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_mix"
    bl_label  = "Change brush blending mode in WP mode to Mix"

    def execute(self, context):
         exit_code = change_wp_bbmode("MIX")
         return exit_code

@registerdcr
class ChangeWPBBmodeToDarken(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_darken"
    bl_label  = "Change brush blending mode in WP mode to Darken"

    def execute(self, context):
         exit_code = change_wp_bbmode("DARKEN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToMul(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_mul"
    bl_label  = "Change brush blending mode in WP mode to Mul"

    def execute(self, context):
         exit_code = change_wp_bbmode("MUL")
         return exit_code

@registerdcr
class ChangeWPBBmodeToColorBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_colorburn"
    bl_label  = "Change brush blending mode in WP mode to Color Burn"

    def execute(self, context):
         exit_code = change_wp_bbmode("COLORBURN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLinearBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_linearburn"
    bl_label  = "Change brush blending mode in WP mode to Linear Burn"

    def execute(self, context):
         exit_code = change_wp_bbmode("LINEARBURN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLighten(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_lighten"
    bl_label  = "Change brush blending mode in WP mode to Lighten"

    def execute(self, context):
         exit_code = change_wp_bbmode("LIGHTEN")
         return exit_code

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

