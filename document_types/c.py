from a import A
from validator import validator
from registry import document_type


@document_type
class C(A):

    @validator
    def c_validator(cls, value):
        if value == "C":
            return True
        else:
            return False
