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

@registerdcr
class ChangeWPBBmodeToScreen(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_screen"
    bl_label  = "Change brush blending mode in WP mode to Screen"

    def execute(self, context):
         exit_code = change_wp_bbmode("SCREEN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToColorDodge(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_colordodge"
    bl_label  = "Change brush blending mode in WP mode to Color Dodge"

    def execute(self, context):
         exit_code = change_wp_bbmode("COLORDODGE")
         return exit_code

@registerdcr
class ChangeWPBBmodeToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_add"
    bl_label  = "Change brush blending mode in WP mode to Add"

    def execute(self, context):
         exit_code = change_wp_bbmode("ADD")
         return exit_code

@registerdcr
class ChangeWPBBmodeToOverlay(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_overlay"
    bl_label  = "Change brush blending mode in WP mode to Overlay"

    def execute(self, context):
         exit_code = change_wp_bbmode("OVERLAY")
         return exit_code

@registerdcr
class ChangeWPBBmodeToSoftLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_softlight"
    bl_label  = "Change brush blending mode in WP mode to Soft Light"

    def execute(self, context):
         exit_code = change_wp_bbmode("SOFTLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToHardLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_hardlight"
    bl_label  = "Change brush blending mode in WP mode to Hard Light"

    def execute(self, context):
         exit_code = change_wp_bbmode("HARDLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToVividLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_vividlight"
    bl_label  = "Change brush blending mode in WP mode to Vivid Light"

    def execute(self, context):
         exit_code = change_wp_bbmode("VIVIDLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLinearLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_linearlight"
    bl_label  = "Change brush blending mode in WP mode to Linear Light"

    def execute(self, context):
         exit_code = change_wp_bbmode("LINEARLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToPinLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_pinlight"
    bl_label  = "Change brush blending mode in WP mode to Pin Light"

    def execute(self, context):
         exit_code = change_wp_bbmode("PINLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToDifference(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_difference"
    bl_label  = "Change brush blending mode in WP mode to Difference"

    def execute(self, context):
         exit_code = change_wp_bbmode("DIFFERENCE")
         return exit_code

@registerdcr
class ChangeWPBBmodeToExclusion(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_exclusion"
    bl_label  = "Change brush blending mode in WP mode to Exclusion"

    def execute(self, context):
         exit_code = change_wp_bbmode("EXCLUSION")
         return exit_code

@registerdcr
class ChangeWPBBmodeToSub(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_sub"
    bl_label  = "Change brush blending mode in WP mode to Sub"

    def execute(self, context):
         exit_code = change_wp_bbmode("SUB")
         return exit_code

@registerdcr
class ChangeWPBBmodeTo(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_hue"
    bl_label  = "Change brush blending mode in WP mode to Hue"

    def execute(self, context):
         exit_code = change_wp_bbmode("HUE")
         return exit_code

@registerdcr
class ChangeWPBBmodeToSaturation(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_saturation"
    bl_label  = "Change brush blending mode in WP mode to Saturation"

    def execute(self, context):
         exit_code = change_wp_bbmode("SATURATION")
         return exit_code

@registerdcr
class ChangeWPBBmodeToColor(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_color"
    bl_label  = "Change brush blending mode in WP mode to Color"

    def execute(self, context):
         exit_code = change_wp_bbmode("COLOR")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLuminosity(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_luminosity"
    bl_label  = "Change brush blending mode in WP mode to Luminosity"

    def execute(self, context):
         exit_code = change_wp_bbmode("LUMINOSITY")
         return exit_code

@registerdcr
class ChangeWPBBmodeToEraseAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_erase_alpha"
    bl_label  = "Change brush blending mode in WP mode to Erase Alpha"

    def execute(self, context):
         exit_code = change_wp_bbmode("ERASE_ALPHA")
         return exit_code

@registerdcr
class ChangeWPBBmodeToAddAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_add_alpha"
    bl_label  = "Change brush blending mode in WP mode to add alpha"

    def execute(self, context):
         exit_code = change_wp_bbmode("ADD_ALPHA")
         return exit_code

def change_wp_bbmode(mode):
    try:
        bpy.data.brushes["Draw"].blend = mode
        return {'FINISHED'}
    except Exception as e:
        print(e)
        return { "CANCELLED" }

