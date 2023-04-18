# Consideren que no pueden modificar este archivo
class NumberDisplay:
    def __init__(self, value,  limit) -> None:
        self.value = value
        self.limit = limit

    def increase(self):
        self.value = (self.value + self.limit + 1) % self.limit
        return self.value == 0

    def reset(self):
        self.value = 0

    def str(self):
        answer = str(self.value)
        if self.value < 10:
            answer = "0" + str(self.value)
        return answer

    def invariant(self):
        return self.value < self.limit

    def clone(self):
        return NumberDisplay(self.value, self.limit)