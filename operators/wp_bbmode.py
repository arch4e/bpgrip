import bpy

from .bbmode   import change_bbmode
from .register import registerdcr

@registerdcr
class ChangeWPBBmodeToMix(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_mix"
    bl_label  = "Change brush blending mode in WP mode to Mix"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "MIX")
         return exit_code

@registerdcr
class ChangeWPBBmodeToDarken(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_darken"
    bl_label  = "Change brush blending mode in WP mode to Darken"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "DARKEN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToMul(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_mul"
    bl_label  = "Change brush blending mode in WP mode to Mul"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "MUL")
         return exit_code

@registerdcr
class ChangeWPBBmodeToColorBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_colorburn"
    bl_label  = "Change brush blending mode in WP mode to Color Burn"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "COLORBURN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLinearBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_linearburn"
    bl_label  = "Change brush blending mode in WP mode to Linear Burn"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "LINEARBURN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLighten(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_lighten"
    bl_label  = "Change brush blending mode in WP mode to Lighten"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "LIGHTEN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToScreen(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_screen"
    bl_label  = "Change brush blending mode in WP mode to Screen"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "SCREEN")
         return exit_code

@registerdcr
class ChangeWPBBmodeToColorDodge(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_colordodge"
    bl_label  = "Change brush blending mode in WP mode to Color Dodge"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "COLORDODGE")
         return exit_code

@registerdcr
class ChangeWPBBmodeToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_add"
    bl_label  = "Change brush blending mode in WP mode to Add"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "ADD")
         return exit_code

@registerdcr
class ChangeWPBBmodeToOverlay(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_overlay"
    bl_label  = "Change brush blending mode in WP mode to Overlay"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "OVERLAY")
         return exit_code

@registerdcr
class ChangeWPBBmodeToSoftLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_softlight"
    bl_label  = "Change brush blending mode in WP mode to Soft Light"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "SOFTLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToHardLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_hardlight"
    bl_label  = "Change brush blending mode in WP mode to Hard Light"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "HARDLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToVividLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_vividlight"
    bl_label  = "Change brush blending mode in WP mode to Vivid Light"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "VIVIDLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLinearLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_linearlight"
    bl_label  = "Change brush blending mode in WP mode to Linear Light"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "LINEARLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToPinLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_pinlight"
    bl_label  = "Change brush blending mode in WP mode to Pin Light"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "PINLIGHT")
         return exit_code

@registerdcr
class ChangeWPBBmodeToDifference(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_difference"
    bl_label  = "Change brush blending mode in WP mode to Difference"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "DIFFERENCE")
         return exit_code

@registerdcr
class ChangeWPBBmodeToExclusion(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_exclusion"
    bl_label  = "Change brush blending mode in WP mode to Exclusion"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "EXCLUSION")
         return exit_code

@registerdcr
class ChangeWPBBmodeToSub(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_sub"
    bl_label  = "Change brush blending mode in WP mode to Sub"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "SUB")
         return exit_code

@registerdcr
class ChangeWPBBmodeTo(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_hue"
    bl_label  = "Change brush blending mode in WP mode to Hue"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "HUE")
         return exit_code

@registerdcr
class ChangeWPBBmodeToSaturation(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_saturation"
    bl_label  = "Change brush blending mode in WP mode to Saturation"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "SATURATION")
         return exit_code

@registerdcr
class ChangeWPBBmodeToColor(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_color"
    bl_label  = "Change brush blending mode in WP mode to Color"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "COLOR")
         return exit_code

@registerdcr
class ChangeWPBBmodeToLuminosity(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_luminosity"
    bl_label  = "Change brush blending mode in WP mode to Luminosity"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "LUMINOSITY")
         return exit_code

@registerdcr
class ChangeWPBBmodeToEraseAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_erase_alpha"
    bl_label  = "Change brush blending mode in WP mode to Erase Alpha"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "ERASE_ALPHA")
         return exit_code

@registerdcr
class ChangeWPBBmodeToAddAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_wp_bbmode_add_alpha"
    bl_label  = "Change brush blending mode in WP mode to add alpha"

    def execute(self, context):
         exit_code = change_bbmode("Draw", "ADD_ALPHA")
         return exit_code
