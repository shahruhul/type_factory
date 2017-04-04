import imp
import os

from registry import registry
from strategies.a import A


def get_type(value):
    for module in registry:
        if module().is_valid(value):
            return module

    return A
