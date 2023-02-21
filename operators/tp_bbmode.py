import bpy

from .bbmode   import change_bbmode
from .register import registerdcr

@registerdcr
class ChangeTPBBmodeToMix(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_mix"
    bl_label  = "Change brush blending mode in TP mode to Mix"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "MIX")
         return exit_code

@registerdcr
class ChangeTPBBmodeToDarken(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_darken"
    bl_label  = "Change brush blending mode in TP mode to Darken"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "DARKEN")
         return exit_code

@registerdcr
class ChangeTPBBmodeToMul(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_mul"
    bl_label  = "Change brush blending mode in TP mode to Mul"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "MUL")
         return exit_code

@registerdcr
class ChangeTPBBmodeToColorBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_colorburn"
    bl_label  = "Change brush blending mode in TP mode to Color Burn"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "COLORBURN")
         return exit_code

@registerdcr
class ChangeTPBBmodeToLinearBurn(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_linearburn"
    bl_label  = "Change brush blending mode in TP mode to Linear Burn"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "LINEARBURN")
         return exit_code

@registerdcr
class ChangeTPBBmodeToLighten(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_lighten"
    bl_label  = "Change brush blending mode in TP mode to Lighten"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "LIGHTEN")
         return exit_code

@registerdcr
class ChangeTPBBmodeToScreen(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_screen"
    bl_label  = "Change brush blending mode in TP mode to Screen"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "SCREEN")
         return exit_code

@registerdcr
class ChangeTPBBmodeToColorDodge(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_colordodge"
    bl_label  = "Change brush blending mode in TP mode to Color Dodge"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "COLORDODGE")
         return exit_code

@registerdcr
class ChangeTPBBmodeToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_add"
    bl_label  = "Change brush blending mode in TP mode to Add"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "ADD")
         return exit_code

@registerdcr
class ChangeTPBBmodeToOverlay(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_overlay"
    bl_label  = "Change brush blending mode in TP mode to Overlay"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "OVERLAY")
         return exit_code

@registerdcr
class ChangeTPBBmodeToSoftLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_softlight"
    bl_label  = "Change brush blending mode in TP mode to Soft Light"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "SOFTLIGHT")
         return exit_code

@registerdcr
class ChangeTPBBmodeToHardLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_hardlight"
    bl_label  = "Change brush blending mode in TP mode to Hard Light"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "HARDLIGHT")
         return exit_code

@registerdcr
class ChangeTPBBmodeToVividLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_vividlight"
    bl_label  = "Change brush blending mode in TP mode to Vivid Light"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "VIVIDLIGHT")
         return exit_code

@registerdcr
class ChangeTPBBmodeToLinearLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_linearlight"
    bl_label  = "Change brush blending mode in TP mode to Linear Light"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "LINEARLIGHT")
         return exit_code

@registerdcr
class ChangeTPBBmodeToPinLight(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_pinlight"
    bl_label  = "Change brush blending mode in TP mode to Pin Light"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "PINLIGHT")
         return exit_code

@registerdcr
class ChangeTPBBmodeToDifference(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_difference"
    bl_label  = "Change brush blending mode in TP mode to Difference"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "DIFFERENCE")
         return exit_code

@registerdcr
class ChangeTPBBmodeToExclusion(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_exclusion"
    bl_label  = "Change brush blending mode in TP mode to Exclusion"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "EXCLUSION")
         return exit_code

@registerdcr
class ChangeTPBBmodeToSub(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_sub"
    bl_label  = "Change brush blending mode in TP mode to Sub"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "SUB")
         return exit_code

@registerdcr
class ChangeTPBBmodeTo(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_hue"
    bl_label  = "Change brush blending mode in TP mode to Hue"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "HUE")
         return exit_code

@registerdcr
class ChangeTPBBmodeToSaturation(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_saturation"
    bl_label  = "Change brush blending mode in TP mode to Saturation"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "SATURATION")
         return exit_code

@registerdcr
class ChangeTPBBmodeToColor(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_color"
    bl_label  = "Change brush blending mode in TP mode to Color"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "COLOR")
         return exit_code

@registerdcr
class ChangeTPBBmodeToLuminosity(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_luminosity"
    bl_label  = "Change brush blending mode in TP mode to Luminosity"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "LUMINOSITY")
         return exit_code

@registerdcr
class ChangeTPBBmodeToEraseAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_erase_alpha"
    bl_label  = "Change brush blending mode in TP mode to Erase Alpha"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "ERASE_ALPHA")
         return exit_code

@registerdcr
class ChangeTPBBmodeToAddAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.change_tp_bbmode_add_alpha"
    bl_label  = "Change brush blending mode in TP mode to add alpha"

    def execute(self, context):
         exit_code = change_bbmode("TexDraw", "ADD_ALPHA")
         return exit_code
