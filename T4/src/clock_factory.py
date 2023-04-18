from .clock_display import ClockDisplay

# Consideren que no pueden modificar este archivo


class ClockFactory:

    def __init__(self) -> None:
        self.cache = {
            "hh:mm": ClockDisplay([24,60]),
            "hh:mm:ss": ClockDisplay([24,60,60]),
            "hh:mm:ss:mmmm": ClockDisplay([24,60,60,1000])}
    
    def create(self, pattern):
        return self.cache[pattern].clone()
