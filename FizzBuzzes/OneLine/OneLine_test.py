import unittest
from contextlib import redirect_stdout
from io import StringIO

from OneLine import fizz_buzz_one_line


class FizzBuzzOneLineTest(unittest.TestCase):

    def test_fb_one_line(self):
        output = StringIO()
        with redirect_stdout(output):
            fizz_buzz_one_line()
        received = output.getvalue()
        for i, line in enumerate(filter(lambda a: a != '', received.split('\n')), start=1):
            if (mod3 := (i % 3 == 0)) & (mod5 := (i % 5 == 0)):
                self.assertTrue(line == 'FizzBuzz')
            elif mod3:
                self.assertTrue(line == 'Fizz')
            elif mod5:
                self.assertTrue(line == 'Buzz')
            else:
                self.assertTrue(line == str(i))


if __name__ == "__main__":
    unittest.main()
