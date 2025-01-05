import bpy
import os

from ..utils.register import registerdcr


@registerdcr
class SetBBmode(bpy.types.Operator):
    bl_idname = 'bpgrip.set_bbmode'
    bl_label  = 'Set brush blending mode'

    # brush blending mode
    brush_blending_mode = [
        ('MIX'        , 'Mix'        , ''),
        ('DARKEN'     , 'Darken'     , ''),
        ('MUL'        , 'Multiply'   , ''),
        ('COLORBURN'  , 'Color Burn' , ''),
        ('LINEARBURN' , 'Linear Burn', ''),
        ('LIGHTEN'    , 'Lighten'    , ''),
        ('SCREEN'     , 'Screen'     , ''),
        ('COLORDODGE' , 'Color Dodge', ''),
        ('ADD'        , 'Add'        , ''),
        ('OVERLAY'    , 'Overlay'    , ''),
        ('SOFTLIGHT'  , 'Soft Light' , ''),
        ('HARDLIGHT'  , 'Hard Light' , ''),
        ('VIVIDLIGHT' , 'Vivid Light', ''),
        ('LINEARLIGHT', 'Liner Light', ''),
        ('PINLIGHT'   , 'Pin Light'  , ''),
        ('DIFFERENCE' , 'Difference' , ''),
        ('EXCLUSION'  , 'Exclusion'  , ''),
        ('SUB'        , 'Subtract'   , ''),
        ('HUE'        , 'Hue'        , ''),
        ('SATURATION' , 'Saturation' , ''),
        ('COLOR'      , 'Color'      , ''),
        ('LUMINOSITY' , 'Value'      , ''),
        ('ERASE_ALPHA', 'Erase Alpha', ''),
        ('ADD_ALPHA'  , 'Add Alpha'  , '')
    ]

    bb_mode: bpy.props.EnumProperty(
        name='Brush Blending Mode', # noqa: F722
        description='Brush Blending Mode', # noqa: F722
        items=brush_blending_mode,
        default='MIX' # noqa: F821
    )

    # get brush asset file path
    resource_path = bpy.utils.resource_path('LOCAL')
    brush_file_path_scl = os.path.join(resource_path, 'datafiles', 'assets', 'brushes', 'essentials_brushes-mesh_sculpt.blend')
    brush_file_path_vtx = os.path.join(resource_path, 'datafiles', 'assets', 'brushes', 'essentials_brushes-mesh_vertex.blend')
    brush_file_path_wei = os.path.join(resource_path, 'datafiles', 'assets', 'brushes', 'essentials_brushes-mesh_weight.blend')
    brush_file_path_tex = os.path.join(resource_path, 'datafiles', 'assets', 'brushes', 'essentials_brushes-mesh_texture.blend')

    def execute(self, context):
        try:
            if context.mode == 'SCULPT':
                bpy.data.brushes['Paint Hard', self.brush_file_path_scl].blend = self.bb_mode
            elif context.mode == 'PAINT_VERTEX':
                bpy.data.brushes['Paint Hard', self.brush_file_path_vtx].blend = self.bb_mode
            elif context.mode == 'PAINT_WEIGHT':
                bpy.data.brushes['Paint', self.brush_file_path_wei].blend = self.bb_mode
            elif context.mode == 'PAINT_TEXTURE':
                bpy.data.brushes['Paint Hard', self.brush_file_path_tex].blend = self.bb_mode

            return {'FINISHED'}
        except Exception as e:
            print(e)
            return { 'CANCELLED' }

