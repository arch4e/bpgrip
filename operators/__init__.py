if "bpy" not in locals():
    import bpy
    from . import wp_bbmode
else:
    import importlib
    importlib.reload(wp_bbmode)
