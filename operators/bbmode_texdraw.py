import bpy

from .bbmode   import set_bbmode
from .register import registerdcr

@registerdcr
class SetBBmodeTexDrawToMix(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_mix"
    bl_label  = "Set brush blending mode to Mix"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "MIX")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToDarken(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_darken"
    bl_label  = "Set brush blending mode to Darken"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "DARKEN")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToMul(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_mul"
    bl_label  = "Set brush blending mode to Mul"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "MUL")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToColorBurn(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_colorburn"
    bl_label  = "Set brush blending mode to Color Burn"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "COLORBURN")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToLinearBurn(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_linearburn"
    bl_label  = "Set brush blending mode to Linear Burn"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "LINEARBURN")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToLighten(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_lighten"
    bl_label  = "Set brush blending mode to Lighten"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "LIGHTEN")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToScreen(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_screen"
    bl_label  = "Set brush blending mode to Screen"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "SCREEN")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToColorDodge(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_colordodge"
    bl_label  = "Set brush blending mode to Color Dodge"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "COLORDODGE")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_add"
    bl_label  = "Set brush blending mode to Add"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "ADD")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToOverlay(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_overlay"
    bl_label  = "Set brush blending mode to Overlay"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "OVERLAY")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToSoftLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_softlight"
    bl_label  = "Set brush blending mode to Soft Light"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "SOFTLIGHT")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToHardLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_hardlight"
    bl_label  = "Set brush blending mode to Hard Light"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "HARDLIGHT")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToVividLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_vividlight"
    bl_label  = "Set brush blending mode to Vivid Light"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "VIVIDLIGHT")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToLinearLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_linearlight"
    bl_label  = "Set brush blending mode to Linear Light"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "LINEARLIGHT")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToPinLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_pinlight"
    bl_label  = "Set brush blending mode to Pin Light"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "PINLIGHT")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToDifference(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_difference"
    bl_label  = "Set brush blending mode to Difference"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "DIFFERENCE")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToExclusion(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_exclusion"
    bl_label  = "Set brush blending mode to Exclusion"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "EXCLUSION")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToSub(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_sub"
    bl_label  = "Set brush blending mode to Sub"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "SUB")
         return exit_code

@registerdcr
class SetBBmodeTexDrawTo(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_hue"
    bl_label  = "Set brush blending mode to Hue"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "HUE")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToSaturation(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_saturation"
    bl_label  = "Set brush blending mode to Saturation"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "SATURATION")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToColor(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_color"
    bl_label  = "Set brush blending mode to Color"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "COLOR")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToLuminosity(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_luminosity"
    bl_label  = "Set brush blending mode to Luminosity"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "LUMINOSITY")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToEraseAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_erase_alpha"
    bl_label  = "Set brush blending mode to Erase Alpha"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "ERASE_ALPHA")
         return exit_code

@registerdcr
class SetBBmodeTexDrawToAddAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_texdraw_add_alpha"
    bl_label  = "Set brush blending mode to add alpha"

    def execute(self, context):
         exit_code = set_bbmode("TexDraw", "ADD_ALPHA")
         return exit_code
