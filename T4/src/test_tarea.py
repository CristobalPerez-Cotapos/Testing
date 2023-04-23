from .clock_display import ClockDisplay
from .clock_factory import ClockFactory
from .display_number import NumberDisplay
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

    # def test_increment_5(self):
    #     factory = ClockFactory()
    #     try:
    #         clock = factory.create("hh")
    #         self.fail()
    #     except KeyError:
    #         pass

    def test_increment_6(self):
        clock = ClockDisplay([1,1])
        try:
            clock.increment()
            self.fail()
        except AssertionError:
            assert(True)

    def test_increase(self):
        number = NumberDisplay(30, 60)
        number.increase()
        self.assertEqual(31, number.value)

    def test_increase_2(self):
        number = NumberDisplay(59, 60)
        number.increase()
        self.assertEqual(0, number.value)

    def test_increase_3(self):
        number = NumberDisplay(-1, 20)
        number.increase()
        self.assertEqual(0, number.value)

    def test_increase_4(self):
        number = NumberDisplay(60, 60)
        number.increase()
        self.assertEqual(1, number.value)
    
    def test_increase_5(self):
        number = NumberDisplay(20, 10)
        number.increase()
        self.assertEqual(1, number.value)

    def test_increase_6(self):
        number = NumberDisplay(-10, 10)
        for i in range(20):
            number.increase()
        self.assertEqual(0, number.value)


    def test_str_1(self):
        number = NumberDisplay(10, 60)
        self.assertEqual("10", number.str())

    def test_str_2(self):
        number = NumberDisplay(9, 60)
        self.assertEqual("09", number.str())

    def test_str_3(self):
        number = NumberDisplay(59, 60)
        self.assertEqual("59", number.str())


    def test_invariant_1(self):
        factory = ClockFactory()
        clock = factory.create("hh:mm")
        self.assertTrue(clock.invariant())

    def test_invariant_2(self):
        number = NumberDisplay(59, 60)
        self.assertTrue(number.invariant())

    def test_invariant_3(self):
        number = NumberDisplay(60, 60)
        self.assertFalse(number.invariant())

    def test_invariant_4(self):
        number = NumberDisplay(20, 10)
        self.assertFalse(number.invariant())


    def test_reset(self):
        number = NumberDisplay(30, 60)
        number.reset()
        self.assertEqual(0, number.value)

    # show that the __init__ method does not return anything
    def test_init_not_return(self):
        number = NumberDisplay(30, 60)
        self.assertEqual(None, number.__init__(30, 60))




    # show that the __init__ method does not return anything
    def test_init_not_return_2(self):
        clock_display = ClockDisplay([23, 60])
        self.assertEqual(None, clock_display.__init__([23, 60]))


if __name__ == '__main__':
    unittest.main()