class binaryOpteration:
    def __init__(self, value):
        self.value = value
    def __and__(self, obj):
        if isinstance(obj, binaryOperation):
            return self.value & obj.value
        else:
            raise ValueError("Must be an object of binaryOperation")

