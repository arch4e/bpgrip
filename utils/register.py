class_list = []


def registerdcr(cls):
    if hasattr(cls, 'bl_rna'):
        class_list.append(cls)
    return cls

