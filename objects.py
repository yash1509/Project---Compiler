class YashObject(object):
    pass


class YashNumber(YashObject):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        assert isinstance(other, YashNumber)
        return YashNumber(self.value + other.value)

    def sub(self, other):
        assert isinstance(other, YashNumber)
        return YashNumber(self.value - other.value)

    def mult(self, other):
        assert isinstance(other, YashNumber)
        return YashNumber(self.value * other.value)

    def div(self, other):
        assert isinstance(other, YashNumber)
        return YashNumber(self.value / other.value)

    def equal(self, other):
        return YashBoolean(self.value == other.value)

    def str(self):
        return str(self.value)


class YashBoolean(YashObject):
    def __init__(self, value):
        assert value in [True, False]
        self.value = value

    def equal(self, other):
        return YashBoolean(self.value == other.value)

    def str(self):
        return "True" if self.value else "False"
