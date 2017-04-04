import pkgutil

registry = []


def _add(cls):
    registry.append(cls)


def document_type(cls):
    _add(cls)
    return cls


def initialize():
    path = ["document_types"]
    name = "document_types"
    for importer, modname, ispkg in pkgutil.walk_packages(path=path, prefix=name+'.'):
        __import__(modname)


initialize()
