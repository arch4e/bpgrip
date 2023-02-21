import bpy

from .bbmode   import change_bbmode
from .register import registerdcr

@registerdcr
class ChangeSPBBmodeToMix(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_mix"
    bl_label  = "Change brush blending mode in SP mode to Mix"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "MIX")
         return exit_code

@registerdcr
class ChangeSPBBmodeToDarken(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_darken"
    bl_label  = "Change brush blending mode in SP mode to Darken"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "DARKEN")
         return exit_code

@registerdcr
class ChangeSPBBmodeToMul(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_mul"
    bl_label  = "Change brush blending mode in SP mode to Mul"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "MUL")
         return exit_code

@registerdcr
class ChangeSPBBmodeToColorBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_colorburn"
    bl_label  = "Change brush blending mode in SP mode to Color Burn"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "COLORBURN")
         return exit_code

@registerdcr
class ChangeSPBBmodeToLinearBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_linearburn"
    bl_label  = "Change brush blending mode in SP mode to Linear Burn"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "LINEARBURN")
         return exit_code

@registerdcr
class ChangeSPBBmodeToLighten(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_lighten"
    bl_label  = "Change brush blending mode in SP mode to Lighten"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "LIGHTEN")
         return exit_code

@registerdcr
class ChangeSPBBmodeToScreen(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_screen"
    bl_label  = "Change brush blending mode in SP mode to Screen"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "SCREEN")
         return exit_code

@registerdcr
class ChangeSPBBmodeToColorDodge(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_colordodge"
    bl_label  = "Change brush blending mode in SP mode to Color Dodge"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "COLORDODGE")
         return exit_code

@registerdcr
class ChangeSPBBmodeToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_add"
    bl_label  = "Change brush blending mode in SP mode to Add"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "ADD")
         return exit_code

@registerdcr
class ChangeSPBBmodeToOverlay(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_overlay"
    bl_label  = "Change brush blending mode in SP mode to Overlay"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "OVERLAY")
         return exit_code

@registerdcr
class ChangeSPBBmodeToSoftLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_softlight"
    bl_label  = "Change brush blending mode in SP mode to Soft Light"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "SOFTLIGHT")
         return exit_code

@registerdcr
class ChangeSPBBmodeToHardLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_hardlight"
    bl_label  = "Change brush blending mode in SP mode to Hard Light"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "HARDLIGHT")
         return exit_code

@registerdcr
class ChangeSPBBmodeToVividLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_vividlight"
    bl_label  = "Change brush blending mode in SP mode to Vivid Light"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "VIVIDLIGHT")
         return exit_code

@registerdcr
class ChangeSPBBmodeToLinearLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_linearlight"
    bl_label  = "Change brush blending mode in SP mode to Linear Light"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "LINEARLIGHT")
         return exit_code

@registerdcr
class ChangeSPBBmodeToPinLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_pinlight"
    bl_label  = "Change brush blending mode in SP mode to Pin Light"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "PINLIGHT")
         return exit_code

@registerdcr
class ChangeSPBBmodeToDifference(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_difference"
    bl_label  = "Change brush blending mode in SP mode to Difference"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "DIFFERENCE")
         return exit_code

@registerdcr
class ChangeSPBBmodeToExclusion(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_exclusion"
    bl_label  = "Change brush blending mode in SP mode to Exclusion"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "EXCLUSION")
         return exit_code

@registerdcr
class ChangeSPBBmodeToSub(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_sub"
    bl_label  = "Change brush blending mode in SP mode to Sub"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "SUB")
         return exit_code

@registerdcr
class ChangeSPBBmodeTo(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_hue"
    bl_label  = "Change brush blending mode in SP mode to Hue"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "HUE")
         return exit_code

@registerdcr
class ChangeSPBBmodeToSaturation(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_saturation"
    bl_label  = "Change brush blending mode in SP mode to Saturation"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "SATURATION")
         return exit_code

@registerdcr
class ChangeSPBBmodeToColor(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_color"
    bl_label  = "Change brush blending mode in SP mode to Color"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "COLOR")
         return exit_code

@registerdcr
class ChangeSPBBmodeToLuminosity(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_luminosity"
    bl_label  = "Change brush blending mode in SP mode to Luminosity"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "LUMINOSITY")
         return exit_code

@registerdcr
class ChangeSPBBmodeToEraseAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_erase_alpha"
    bl_label  = "Change brush blending mode in SP mode to Erase Alpha"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "ERASE_ALPHA")
         return exit_code

@registerdcr
class ChangeSPBBmodeToAddAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_sp_bbmode_add_alpha"
    bl_label  = "Change brush blending mode in SP mode to add alpha"

    def execute(self, context):
         exit_code = change_bbmode("Paint", "ADD_ALPHA")
         return exit_code
