if "bpy" not in locals():
    import bpy
    from . import tp_bbmode
    from . import wp_bbmode
else:
    import importlib
    importlib.reload(tp_bbmode)
    importlib.reload(wp_bbmode)
