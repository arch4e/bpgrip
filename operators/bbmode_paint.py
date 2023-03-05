import bpy

from .bbmode   import set_bbmode
from .register import registerdcr

@registerdcr
class SetBBmodePaintToMix(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_mix"
    bl_label  = "Set brush blending mode to Mix"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "MIX")
         return exit_code

@registerdcr
class SetBBmodePaintToDarken(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_darken"
    bl_label  = "Set brush blending mode to Darken"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "DARKEN")
         return exit_code

@registerdcr
class SetBBmodePaintToMul(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_mul"
    bl_label  = "Set brush blending mode to Mul"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "MUL")
         return exit_code

@registerdcr
class SetBBmodePaintToColorBurn(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_colorburn"
    bl_label  = "Set brush blending mode to Color Burn"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "COLORBURN")
         return exit_code

@registerdcr
class SetBBmodePaintToLinearBurn(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_linearburn"
    bl_label  = "Set brush blending mode to Linear Burn"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "LINEARBURN")
         return exit_code

@registerdcr
class SetBBmodePaintToLighten(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_lighten"
    bl_label  = "Set brush blending mode to Lighten"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "LIGHTEN")
         return exit_code

@registerdcr
class SetBBmodePaintToScreen(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_screen"
    bl_label  = "Set brush blending mode to Screen"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "SCREEN")
         return exit_code

@registerdcr
class SetBBmodePaintToColorDodge(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_colordodge"
    bl_label  = "Set brush blending mode to Color Dodge"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "COLORDODGE")
         return exit_code

@registerdcr
class SetBBmodePaintToAdd(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_add"
    bl_label  = "Set brush blending mode to Add"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "ADD")
         return exit_code

@registerdcr
class SetBBmodePaintToOverlay(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_overlay"
    bl_label  = "Set brush blending mode to Overlay"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "OVERLAY")
         return exit_code

@registerdcr
class SetBBmodePaintToSoftLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_softlight"
    bl_label  = "Set brush blending mode to Soft Light"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "SOFTLIGHT")
         return exit_code

@registerdcr
class SetBBmodePaintToHardLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_hardlight"
    bl_label  = "Set brush blending mode to Hard Light"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "HARDLIGHT")
         return exit_code

@registerdcr
class SetBBmodePaintToVividLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_vividlight"
    bl_label  = "Set brush blending mode to Vivid Light"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "VIVIDLIGHT")
         return exit_code

@registerdcr
class SetBBmodePaintToLinearLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_linearlight"
    bl_label  = "Set brush blending mode to Linear Light"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "LINEARLIGHT")
         return exit_code

@registerdcr
class SetBBmodePaintToPinLight(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_pinlight"
    bl_label  = "Set brush blending mode to Pin Light"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "PINLIGHT")
         return exit_code

@registerdcr
class SetBBmodePaintToDifference(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_difference"
    bl_label  = "Set brush blending mode to Difference"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "DIFFERENCE")
         return exit_code

@registerdcr
class SetBBmodePaintToExclusion(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_exclusion"
    bl_label  = "Set brush blending mode to Exclusion"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "EXCLUSION")
         return exit_code

@registerdcr
class SetBBmodePaintToSub(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_sub"
    bl_label  = "Set brush blending mode to Sub"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "SUB")
         return exit_code

@registerdcr
class SetBBmodePaintTo(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_hue"
    bl_label  = "Set brush blending mode to Hue"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "HUE")
         return exit_code

@registerdcr
class SetBBmodePaintToSaturation(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_saturation"
    bl_label  = "Set brush blending mode to Saturation"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "SATURATION")
         return exit_code

@registerdcr
class SetBBmodePaintToColor(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_color"
    bl_label  = "Set brush blending mode to Color"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "COLOR")
         return exit_code

@registerdcr
class SetBBmodePaintToLuminosity(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_luminosity"
    bl_label  = "Set brush blending mode to Luminosity"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "LUMINOSITY")
         return exit_code

@registerdcr
class SetBBmodePaintToEraseAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_erase_alpha"
    bl_label  = "Set brush blending mode to Erase Alpha"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "ERASE_ALPHA")
         return exit_code

@registerdcr
class SetBBmodePaintToAddAlpha(bpy.types.Operator):
    bl_idname = "bpgrip.set_bbmode_paint_add_alpha"
    bl_label  = "Set brush blending mode to add alpha"

    def execute(self, context):
         exit_code = set_bbmode("Paint", "ADD_ALPHA")
         return exit_code
