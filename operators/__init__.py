if "bpy" not in locals():
    import bpy
    from . import bbmode
else:
    import importlib
    importlib.reload(bbmode)
