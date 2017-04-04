import pkgutil

registry = []


def _add(cls):
    registry.append(cls)


def document_type(cls):
    _add(cls)
    return cls


def initialize():
    path = ["strategies"]
    name = "strategies"
    for importer, modname, ispkg in pkgutil.walk_packages(path=path, prefix=name+'.'):
        __import__(modname)


initialize()
