import bpy

def change_bbmode(bl_mode, bb_mode):
    try:
        bpy.data.brushes[bl_mode].blend = bb_mode
        return {'FINISHED'}
    except Exception as e:
        print(e)
        return { "CANCELLED" }
