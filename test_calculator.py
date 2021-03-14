import calculator


class TestCalculator:

    def test_addition(self):
        assert(calculator.addition(2, 3) == 5)

    def test_subtraction(self):
        assert(calculator.subtraction(2, 3) == -1)

    def test_multiplication(self):
        assert(calculator.multiplication(2, 3) == 6)

    def test_division(self):
        assert(calculator.division(10, 5) == 2)
