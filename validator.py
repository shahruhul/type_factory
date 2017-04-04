def validator(func):
    func.validator = True
    return func
