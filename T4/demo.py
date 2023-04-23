from src.clock_factory import ClockFactory

# Archivo demo del reloj funcionando lo pueden eliminar si quieren

factory = ClockFactory()
clock = factory.create("hh:mm")

for i in range(10000):
    clock.increment()
    print(clock.str())
