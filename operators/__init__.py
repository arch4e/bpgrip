if "bpy" not in locals():
    from . import bbmode
else:
    import importlib
    importlib.reload(bbmode)

