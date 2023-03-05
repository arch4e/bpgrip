# -*- coding: utf-8 -*-

bl_info = {
    "name"    : "bpgrip",
    "category": "3D View",
    "location": "",
    "version" : (1,0),
    "blender" : (3,0,0),
    "author"  : "ShioN"
}

if "bpy" not in locals():
    import bpy
    from . import operators
else:
    import importlib
    importlib.reload(operators)

def check_blender_version():
    if bpy.app.version < bl_info.get("blender"):
        unregister()
        raise ImportError("error: unsupported version")

def register():
    # Returns an exception current Blender version is not supported
    check_blender_version()

    try:
        for cls in operators.register.class_list:
            bpy.utils.register_class(cls)
    except Exception as e:
        print("error: registration failed")
        print(repr(e))
        pass

def unregister():
    try:
        for cls in reversed(operators.register.class_list):
            bpy.utils.unregister_class(cls)
    except Exception:
        print("error: unregistration failed")
        pass

if __name__ == "__main__":
    register()

