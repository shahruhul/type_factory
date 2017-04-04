import pdb
from validator import validator

class A(object):

    @validator
    def a_validator(cls, values):
        return True

    def is_valid(cls, values):
	names = [method for method in dir(cls) if hasattr(getattr(cls, method), 'validator')]
	functions = [getattr(cls, name) for name in names]

        valid = True
	for func in functions:
            valid = valid and func(values)

        return valid
