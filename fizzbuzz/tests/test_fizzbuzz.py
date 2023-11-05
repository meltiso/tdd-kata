from src.fizzbuzz import FizzBuzz

class TestFizzBuzz:
    def test_do_nothing(self):
        assert isinstance(FizzBuzz(), FizzBuzz)
