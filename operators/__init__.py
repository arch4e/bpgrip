if "bpy" not in locals():
    import bpy
    from . import bbmode_draw
    from . import bbmode_paint
    from . import bbmode_texdraw
else:
    import importlib
    importlib.reload(bbmode_draw)
    importlib.reload(bbmode_paint)
    importlib.reload(bbmode_texdraw)
