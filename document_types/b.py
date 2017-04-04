from a import A
from validator import validator
from registry import document_type

@document_type
class B(A):

    @validator
    def b_validator(cls, values):
        print (values)
        if values == "B":
            return True
        else:
            return False
