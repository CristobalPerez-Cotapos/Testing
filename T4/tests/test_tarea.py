from src.clock_factory import *
from src.clock_display import *
from src.display_number import *
import unittest



class TestClockFactory(unittest.TestCase):

    def test_create(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        self.assertEqual(clock.str(), "00:00")

    def test_create_2(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm:ss")
        self.assertEqual(clock.str(), "00:00:00")

    def test_create_3(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm:ss:mmmm")
        self.assertEqual(clock.str(), "00:00:00:00")

    def test_increment_1(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        clock.increment()
        self.assertEqual(clock.str(), "00:01")

    def test_increment_2(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm:ss")
        clock.increment()
        self.assertEqual(clock.str(), "00:00:01")

    def test_increment_3(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm:ss:mmmm")
        clock.increment()
        self.assertEqual(clock.str(), "00:00:00:01")

    def test_increment_4(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        for i in range(60):
            clock.increment()
        self.assertEqual(clock.str(), "01:00")

    def test_invariant_1(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        self.assertTrue(clock.invariant())


    def test_reset(self):
        number = NumberDisplay(30, 60)
        number.reset()
        self.assertEqual(0, number.value)



if __name__ == '__main__':
    unittest.main()