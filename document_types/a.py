import pdb
from validator import validator

class A(object):

    @validator
    def a_validator(cls, values):
        return True

    def is_valid(cls, values):
	names = [method for method in dir(cls) if hasattr(getattr(cls, method), 'validator')]

        valid = True

        for name in names:
            func = getattr(cls, name)
            valid = valid and func(values)

        return valid
