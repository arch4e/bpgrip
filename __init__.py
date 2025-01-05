# -*- coding: utf-8 -*-


bl_info = {
    'name'    : 'bpgrip',
    'category': '3D View',
    'location': '',
    'version' : (2,0),
    'blender' : (3,0,0),
    'author'  : 'ShioN'
}


if 'bpy' not in locals():
    import bpy
    from . import operators
    from . import utils
else:
    import importlib
    importlib.reload(operators)
    importlib.reload(utils)


def register():
    try:
        for cls in utils.register.class_list:
            bpy.utils.register_class(cls)
    except Exception as e:
        print('error: registration failed')
        print(repr(e))
        pass


def unregister():
    try:
        for cls in reversed(utils.register.class_list):
            bpy.utils.unregister_class(cls)
    except Exception:
        print('error: unregistration failed')
        pass


if __name__ == '__main__':
    register()

