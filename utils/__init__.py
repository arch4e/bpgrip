if 'bpy' not in locals():
    from . import register
else:
    import importlib
    importlib.reload(register)

