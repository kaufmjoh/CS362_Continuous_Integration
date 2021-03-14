import calculator


class TestCalculator:

    def test_addition(self):
        assert(calculator.addition(2, 3) == 5)

    def test_subtraction(self):
        assert(calculator.subtraction(2, 3) == -1)
