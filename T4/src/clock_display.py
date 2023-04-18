from .display_number import NumberDisplay

# Consideren que no pueden modificar este archivo


class ClockDisplay:
    def __init__(self, limitValues) -> None:
        self.numbers = list(map(lambda limit: NumberDisplay(0,limit),limitValues))

    def increment(self):
        currentDisplay = len(self.numbers) - 1
        while currentDisplay >= 0 and self.numbers[currentDisplay].increase():
            currentDisplay -= 1

    def str(self):
        return ':'.join(map(lambda n: n.str(), self.numbers))
    
    def clone(self):
        clone = ClockDisplay([23, 60])
        clone.numbers = list(map(lambda n: n.clone(), self.numbers))
        return clone

    def invariant(self):
        return all(number.invariant() for number in self.numbers)