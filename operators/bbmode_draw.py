import bpy

from .bbmode   import set_bbmode
from .register import registerdcr

@registerdcr
class SetBBmodeDrawToMix(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_mix"
    bl_label  = "Set brush blending mode to Mix"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "MIX")
         return exit_code

@registerdcr
class SetBBmodeDrawToDarken(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_darken"
    bl_label  = "Set brush blending mode to Darken"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "DARKEN")
         return exit_code

@registerdcr
class SetBBmodeDrawToMul(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_mul"
    bl_label  = "Set brush blending mode to Mul"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "MUL")
         return exit_code

@registerdcr
class SetBBmodeDrawToColorBurn(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_colorburn"
    bl_label  = "Set brush blending mode to Color Burn"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "COLORBURN")
         return exit_code

@registerdcr
class SetBBmodeDrawToLinearBurn(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_linearburn"
    bl_label  = "Set brush blending mode to Linear Burn"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "LINEARBURN")
         return exit_code

@registerdcr
class SetBBmodeDrawToLighten(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_lighten"
    bl_label  = "Set brush blending mode to Lighten"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "LIGHTEN")
         return exit_code

@registerdcr
class SetBBmodeDrawToScreen(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_screen"
    bl_label  = "Set brush blending mode to Screen"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "SCREEN")
         return exit_code

@registerdcr
class SetBBmodeDrawToColorDodge(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_colordodge"
    bl_label  = "Set brush blending mode to Color Dodge"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "COLORDODGE")
         return exit_code

@registerdcr
class SetBBmodeDrawToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_add"
    bl_label  = "Set brush blending mode to Add"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "ADD")
         return exit_code

@registerdcr
class SetBBmodeDrawToOverlay(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_overlay"
    bl_label  = "Set brush blending mode to Overlay"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "OVERLAY")
         return exit_code

@registerdcr
class SetBBmodeDrawToSoftLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_softlight"
    bl_label  = "Set brush blending mode to Soft Light"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "SOFTLIGHT")
         return exit_code

@registerdcr
class SetBBmodeDrawToHardLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_hardlight"
    bl_label  = "Set brush blending mode to Hard Light"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "HARDLIGHT")
         return exit_code

@registerdcr
class SetBBmodeDrawToVividLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_vividlight"
    bl_label  = "Set brush blending mode to Vivid Light"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "VIVIDLIGHT")
         return exit_code

@registerdcr
class SetBBmodeDrawToLinearLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_linearlight"
    bl_label  = "Set brush blending mode to Linear Light"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "LINEARLIGHT")
         return exit_code

@registerdcr
class SetBBmodeDrawToPinLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_pinlight"
    bl_label  = "Set brush blending mode to Pin Light"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "PINLIGHT")
         return exit_code

@registerdcr
class SetBBmodeDrawToDifference(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_difference"
    bl_label  = "Set brush blending mode to Difference"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "DIFFERENCE")
         return exit_code

@registerdcr
class SetBBmodeDrawToExclusion(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_exclusion"
    bl_label  = "Set brush blending mode to Exclusion"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "EXCLUSION")
         return exit_code

@registerdcr
class SetBBmodeDrawToSub(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_sub"
    bl_label  = "Set brush blending mode to Sub"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "SUB")
         return exit_code

@registerdcr
class SetBBmodeDrawTo(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_hue"
    bl_label  = "Set brush blending mode to Hue"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "HUE")
         return exit_code

@registerdcr
class SetBBmodeDrawToSaturation(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_saturation"
    bl_label  = "Set brush blending mode to Saturation"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "SATURATION")
         return exit_code

@registerdcr
class SetBBmodeDrawToColor(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_color"
    bl_label  = "Set brush blending mode to Color"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "COLOR")
         return exit_code

@registerdcr
class SetBBmodeDrawToLuminosity(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_luminosity"
    bl_label  = "Set brush blending mode to Luminosity"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "LUMINOSITY")
         return exit_code

@registerdcr
class SetBBmodeDrawToEraseAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_erase_alpha"
    bl_label  = "Set brush blending mode to Erase Alpha"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "ERASE_ALPHA")
         return exit_code

@registerdcr
class SetBBmodeDrawToAddAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_draw_add_alpha"
    bl_label  = "Set brush blending mode to add alpha"

    def execute(self, context):
         exit_code = set_bbmode("Draw", "ADD_ALPHA")
         return exit_code
